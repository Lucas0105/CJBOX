# Generated by Django 3.2.13 on 2022-11-21 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_alter_movie_backdrop_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='backdrop_path',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]