from django.db import models
from account.models import User


class Category(models.Model):
    category = models.CharField(verbose_name="分類", max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name="登録日時", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="修正時間", auto_now=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = "Categories"


class Faq(models.Model):
    question = models.CharField(verbose_name="質問", max_length=200)
    answer = models.TextField(verbose_name="返事")
    author = models.ForeignKey(User, verbose_name="登録", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name="分類", on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(verbose_name="登録日時", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="修正時間", auto_now=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = "Frequent Answers and Questions"

