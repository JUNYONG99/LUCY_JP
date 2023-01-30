from django.db import models
from account.models import User
from django.db.models import Avg


# 카테고리 모델
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/shop/category/{self.slug}/'

    class Meta:
        verbose_name_plural = 'Categories'

# 일본 카테고리 모델
class CategoryJP(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/shop/category/jp/{self.slug}/'

    class Meta:
        verbose_name_plural = 'Categories JP'

# 브랜드 모델
class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)
    logo_img = models.ImageField(upload_to='shop/brands/%Y/%m/%d/', null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/shop/brand/{self.slug}/'


# 상품 모델
class Product(models.Model):
    signature_img = models.ImageField(upload_to='shop/images/%Y/%m/%d/')
    title = models.CharField(max_length=30)  # 상품명
    price = models.IntegerField(default=0)  # 상품 가격
    qty = models.PositiveSmallIntegerField(null=False, default=1)  # 상품 수량
    info = models.TextField(max_length=200, null=False)  # 상품 소개
    like_count = models.IntegerField(default=0)  # 좋아요 수
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(
        Category, blank=True)
    brand = models.ForeignKey(
        Brand, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self):
        return f'/shop/{self.pk}/'

    def average_review(self):  # 리뷰 평균 평점
        reviews = Review.objects.filter(product=self).aggregate(average=Avg('rate'))
        avg = 0
        if reviews['average'] is not None:
            avg = round(float(reviews['average']), 2)
        return avg

    def count_review(self):  # 리뷰 수
        count_review = Review.objects.filter(product=self).count()
        return count_review

    @property  # 리뷰 정렬
    def get_reviews(self):
        return self.reviews.all().order_by('-created_at')


# 좋아요 모델
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product} - {self.user}'

    def get_absolute_url(self):
        return f'{self.product.get_absolute_url()}#like-{self.pk}'


# 상품평 모델
class Review(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.FloatField()

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'[{self.pk}][{self.product.title}] - {self.user.nickname} :{self.rate}'

    def get_absolute_url(self):
        return f'{self.product.get_absolute_url()}{self.pk}'


# 상품 문의 모델
class Inquiry(models.Model):
    content = models.TextField()
#    secret = models.BooleanField(default=False)
    answer = models.TextField(null=True)
    answered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Inquiries'

    def __str__(self):
        return f'[{self.pk}][{self.product.title}] - 문의자 : {self.user.nickname}'

    def get_absolute_url(self):
        return f'{self.product.get_absolute_url()}{self.pk}'


# 장바구니 모델
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'[{self.pk}] 상품-{self.product.title} | 사용자-{self.user.nickname} | 수량-{self.product_qty}'

    # 해당 상품 개수에 맞춰 가격 변동
    def sub_total(self):
        return self.product.price * self.product_qty
