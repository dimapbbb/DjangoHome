# Generated by Django 5.0.7 on 2024-08-20 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userpost',
            old_name='image',
            new_name='picture',
        ),
    ]
