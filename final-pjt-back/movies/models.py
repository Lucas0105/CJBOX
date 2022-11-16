from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    reviews = models.ManyToManyField(settings.AUTH_USER_MODEL, through='reviews.Review', related_name='reviews')
    movie_id = models.IntegerField()
    poster_path = models.CharField(max_length=100)
    backdrop_path = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.CharField(max_length=50)
    vote_average = models.IntegerField()