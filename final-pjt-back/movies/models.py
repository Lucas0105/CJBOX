from django.db import models

# Create your models here.
class Model(models.Model):
    movie_id = models.IntegerField()
    poster_path = models.CharField(max_length=100)
    backdrop_path = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.CharField(max_length=50)
    vote_average = models.IntegerField()