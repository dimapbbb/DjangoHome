# Generated by Django 5.0.7 on 2024-08-20 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_remove_product_manufactured_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products_photo', verbose_name='Изображение'),
        ),
    ]
