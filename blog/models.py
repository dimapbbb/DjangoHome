from django.db import models
import datetime


class UserPost(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    slug = models.CharField(max_length=150, verbose_name="slug", blank=True, null=True)
    content = models.TextField(verbose_name="Содержимое")
    picture = models.ImageField(upload_to="blog_picture/", verbose_name="Картинка", blank=True, null=True)
    creation_date = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    publication_sign = models.BooleanField(default=False, verbose_name="Знак публикации")
    views_count = models.IntegerField(default=0, verbose_name="Просмотры")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Blog"
