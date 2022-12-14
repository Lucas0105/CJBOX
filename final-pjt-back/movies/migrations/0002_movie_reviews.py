# Generated by Django 3.2.13 on 2022-11-16 08:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='reviews',
            field=models.ManyToManyField(related_name='reviews', through='reviews.Review', to=settings.AUTH_USER_MODEL),
        ),
    ]
