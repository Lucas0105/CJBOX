# Generated by Django 3.2.13 on 2022-11-21 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_alter_movie_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='backdrop_path',
            field=models.CharField(default='', max_length=100),
        ),
    ]
