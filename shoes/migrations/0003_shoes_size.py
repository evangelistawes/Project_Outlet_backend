# Generated by Django 4.2 on 2023-06-10 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0002_shoes_photo_shoes_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoes',
            name='size',
            field=models.JSONField(default=[]),
        ),
    ]
