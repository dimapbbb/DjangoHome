# Generated by Django 5.0.7 on 2024-08-05 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='manufactured_at',
            field=models.DateField(blank=True, null=True, verbose_name='Дата производства'),
        ),
    ]
