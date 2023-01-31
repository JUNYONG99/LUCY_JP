from django.db import models
from account.models import User
from django.db.models import Avg


# カテゴリー
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/shop/category/{self.slug}/'

    class Meta:
        verbose_name_plural = 'Categories'


# ブランド
class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)
    logo_img = models.ImageField(upload_to='shop/brands/%Y/%m/%d/', null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/shop/brand/{self.slug}/'


# 商品
class Product(models.Model):
    signature_img = models.ImageField(verbose_name="商品イメージ",upload_to='shop/images/%Y/%m/%d/')
    title = models.CharField(verbose_name="商品名", max_length=30)  
    price = models.IntegerField(verbose_name="価格", default=0)  
    qty = models.PositiveSmallIntegerField(verbose_name="カート商品", null=False, default=1)  
    info = models.TextField(verbose_name="商品詳細", max_length=200, null=False)  
    like_count = models.IntegerField(verbose_name="お気に入り数", default=0)  
    created_at = models.DateTimeField(verbose_name="登録日時", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="修正時間", auto_now=True)
    category = models.ManyToManyField(
        Category, blank=True, verbose_name="カテゴリー")
    brand = models.ForeignKey(
        Brand, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="ブランド")

    def __str__(self):
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self):
        return f'/shop/{self.pk}/'

    def average_review(self):  # レビュー評価平均
        reviews = Review.objects.filter(product=self).aggregate(average=Avg('rate'))
        avg = 0
        if reviews['average'] is not None:
            avg = round(float(reviews['average']), 2)
        return avg

    def count_review(self):  # レビュー数
        count_review = Review.objects.filter(product=self).count()
        return count_review

    @property  # レビュー整列
    def get_reviews(self):
        return self.reviews.all().order_by('-created_at')


# お気に入り
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="会員")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="商品")

    def __str__(self):
        return f'{self.product} - {self.user}'

    def get_absolute_url(self):
        return f'{self.product.get_absolute_url()}#like-{self.pk}'


# レビュー
class Review(models.Model):
    content = models.TextField(verbose_name="内容")
    created_at = models.DateTimeField(verbose_name="登録日時", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="修正時間", auto_now=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name="会員")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="商品")
    rate = models.FloatField(verbose_name="評価")

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'[{self.pk}][{self.product.title}] - {self.user.nickname} :{self.rate}'

    def get_absolute_url(self):
        return f'{self.product.get_absolute_url()}{self.pk}'


# お問い合わせ
class Inquiry(models.Model):
    content = models.TextField(verbose_name="内容")
    answer = models.TextField(verbose_name="返信", null=True)
    answered = models.BooleanField(verbose_name="返信確認", default=False)
    created_at = models.DateTimeField(verbose_name="登録日時", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="登修正日時", auto_now=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name="会員")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="商品")

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Inquiries'

    def __str__(self):
        return f'[{self.pk}][{self.product.title}] - 問い合わせ者 : {self.user.nickname}'

    def get_absolute_url(self):
        return f'{self.product.get_absolute_url()}{self.pk}'


# ショッピングカート
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="会員")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="商品")
    product_qty = models.IntegerField(verbose_name="商品数量")
    created_at = models.DateTimeField(verbose_name="登録日時", auto_now_add=True)

    def __str__(self):
        return f'[{self.pk}] 商品-{self.product.title} | 会員-{self.user.nickname} | 数量 -{self.product_qty}'

    # 商品の数量に合わせて金額変更
    def sub_total(self):
        return format(self.product.price * self.product_qty, ',')
