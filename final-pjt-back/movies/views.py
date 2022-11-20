from .serializers import MovieListSerializer, MovieSearchSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Movie, Genre, UserLikeGenres
import random


@extend_schema(responses=MovieListSerializer)
@api_view(['GET'])
def popular(request):
    movies = Movie.objects.all().order_by('-popularity')[:15]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@extend_schema(responses=MovieListSerializer)
@api_view(['GET'])
def newMovie(request, page):
    movies = Movie.objects.all().order_by('-release_date')[(page-1) * 9:9*page]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@extend_schema(responses=MovieSearchSerializer)
@api_view(['GET'])
def search(request, title):
    movies = Movie.objects.filter(title__contains=title)[:10]
    serializer = MovieSearchSerializer(movies, many=True)
    return Response(serializer.data)


@extend_schema(responses=MovieListSerializer)
@api_view(['GET'])
def detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    serializer = MovieListSerializer(movie)
    return Response(serializer.data)


@extend_schema(responses=MovieListSerializer)
@api_view(['GET'])
def genre(request, genre, page):
    genre = get_object_or_404(Genre, name=genre)
    movies = Movie.objects.filter(genres=genre).all()[(page-1) * 9:9*page]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


def recommendAnonymous():
    index = [i for i in range(100)]
    movies = Movie.objects.order_by('-vote_average', '-release_date', '-popularity')[:100]
    movie_data = []

    index = random.sample(index, 15)

    for i in index:
        movie_data.append(movies[i])
    return MovieListSerializer(movie_data, many=True)


@extend_schema(responses=MovieListSerializer)
@api_view(['GET'])
def recommend(request):

    if request.user.is_anonymous:

        serializer = recommendAnonymous()

        return Response(serializer.data)
    else:
        rand_filter = ['-popularity', '-release_date', '-vote_average', '?']

        user = request.user

        genres = UserLikeGenres.objects.filter(user=user).order_by('-count')[:3]
        if len(genres):
            index = random.randrange(0, len(genres))
            genre = genres[index].genre
            movies = Movie.objects.filter(genres=genre).order_by(random.sample(rand_filter, 1)[0])[:15]
            serializer = MovieListSerializer(movies, many=True)

        else:
            serializer = recommendAnonymous()

        return Response(serializer.data)


@extend_schema(responses=MovieListSerializer)
@api_view(['GET'])
def recommendGenre(request, genre):
    rand_filter = ['-popularity', '-release_date', '-vote_average']
    genre = get_object_or_404(Genre, name=genre)
    movies = Movie.objects.filter(genres=genre).order_by(random.sample(rand_filter, 1)[0])[:15]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


