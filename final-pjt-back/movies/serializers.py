from rest_framework import serializers
from .models import Movie, Genre


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name', 'id')


class MovieListSerializer(serializers.ModelSerializer):

    genres = GenreSerializer(many=True, read_only = True)

    class Meta:
        model = Movie
        fields = '__all__'


class MovieSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('poster_path', 'title', 'id',)
