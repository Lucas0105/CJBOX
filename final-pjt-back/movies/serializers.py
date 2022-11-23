from rest_framework import serializers
from .models import Movie, Genre
from django.contrib.auth import get_user_model


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name', 'id')


class MovieListSerializer(serializers.ModelSerializer):

    class UserNameSerializer(serializers.ModelSerializer):

        class Meta:
            model = get_user_model()
            fields = ('nickname',)

    like_users = UserNameSerializer(many=True, read_only = True)
    genres = GenreSerializer(many=True, read_only = True)

    class Meta:
        model = Movie
        fields = '__all__'


class MovieSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('poster_path', 'title', 'id',)
