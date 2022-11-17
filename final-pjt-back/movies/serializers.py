from rest_framework import serializers
from .models import Movie

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('poster_path', 'title', 'overview', 'vote_average', 'popularity')
