from django.db import models
from django.conf import settings


class Review(models.Model):
    movie = models.ForeignKey('movies.Movie', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='review_likes')
    content = models.TextField()
    vote = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comment')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comment')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


