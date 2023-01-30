from django.db import models
from account.models import User

class About(models.Model):
    title = models.CharField(verbose_name="제목", max_length=200)
    content = models.TextField(verbose_name="내용")
    author = models.ForeignKey(User, verbose_name="등록", on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name="등록일시", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="수정일시", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "About"
