# Generated by Django 4.2 on 2023-04-08 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='opinions',
        ),
    ]