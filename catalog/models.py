from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование категории")
    description = models.TextField(verbose_name="Описание категории")

    def __str__(self):
        return f"{self.name} {self.description}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, verbose_name="Наименование продукта")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="products_photo", verbose_name="Изображение", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name="Products")
    price = models.IntegerField(verbose_name="Цена")
    is_published = models.BooleanField(default=False, verbose_name="Признак публикации")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(auto_now=True, verbose_name="Дата изменения")

    def __str__(self):
        return f"{self.name} {self.price} {self.description}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        permissions = [
            ("can_change_publication", "can_change_publication"),
            ("can_change_description", "can_change_description"),
            ("can_change_category", "can_change_category")
        ]


class Version(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название версии")
    number = models.CharField(max_length=10, verbose_name="Номер версии")
    current = models.BooleanField(verbose_name="Признак текущей версии")

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.number}"

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
