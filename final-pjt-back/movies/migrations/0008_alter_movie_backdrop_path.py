# Generated by Django 3.2.13 on 2022-11-21 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_alter_movie_backdrop_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='backdrop_path',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]
