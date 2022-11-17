from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=100)
    userLikeGenres = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likeGenres', through='UserLikeGenres')

class UserLikeGenres(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

# Create your models here.
class Movie(models.Model):
    genres = models.ManyToManyField(Genre, related_name='movies')
    reviews = models.ManyToManyField(settings.AUTH_USER_MODEL, through='reviews.Review', related_name='reviews')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='my_lists')
    poster_path = models.CharField(max_length=100)
    backdrop_path = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.CharField(max_length=50)
    vote_average = models.IntegerField()
    popularity = models.IntegerField()
    vote_count = models.IntegerField()