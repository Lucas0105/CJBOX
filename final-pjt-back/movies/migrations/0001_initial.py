# Generated by Django 3.2.13 on 2022-11-16 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField()),
                ('poster_path', models.CharField(max_length=100)),
                ('backdrop_path', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('overview', models.TextField()),
                ('release_date', models.CharField(max_length=50)),
                ('vote_average', models.IntegerField()),
            ],
        ),
    ]
