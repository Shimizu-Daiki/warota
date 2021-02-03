from django.db import models
from django.core import validators

class  User(models.Model):

    name = models.CharField(
        verbose_name='名前',
        max_length=200,
    )

    created_at = models.DateTimeField(
        verbose_name='登録日',
        auto_now_add=True
    )

    # 以下は管理サイト上の表示設定
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ユーザー'
        verbose_name_plural = 'ユーザー'

class Problem(models.Model):

    name = models.CharField(
        verbose_name='登録者名',
        max_length=20,
    )

    text = models.TextField(
        verbose_name='早口言葉を入力',
        max_length=100,
        blank=False,
        null=False,
    )
    created_at = models.DateTimeField(
        verbose_name='登録日',
        auto_now_add=True
    )

    # 以下は管理サイト上の表示設定
    def __str__(self):
        return self.text.verbose_name

    class Meta:
        verbose_name = '問題'
        verbose_name_plural = '問題'

# Create your models here.
