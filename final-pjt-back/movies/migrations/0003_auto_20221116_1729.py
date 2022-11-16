# Generated by Django 3.2.13 on 2022-11-16 08:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0002_movie_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='like_users',
            field=models.ManyToManyField(related_name='my_lists', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='UserLikeGenres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.genre')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='genre',
            name='userLikeGenres',
            field=models.ManyToManyField(related_name='likeGenres', through='movies.UserLikeGenres', to=settings.AUTH_USER_MODEL),
        ),
    ]
