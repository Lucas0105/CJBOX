# Generated by Django 3.2.13 on 2022-11-17 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20221117_0909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='movie_id',
        ),
    ]
