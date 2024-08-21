# Generated by Django 5.0.7 on 2024-08-20 18:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_userpost_creation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 20, 21, 44, 14, 712515), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='blog_picture', verbose_name='Картинка'),
        ),
    ]
