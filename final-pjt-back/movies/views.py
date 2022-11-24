from .serializers import MovieListSerializer, MovieSearchSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404
from reviews.models import Review
from .models import Movie, Genre, UserLikeGenres
import requests
import random
import math
import os


@extend_schema(responses=MovieListSerializer)
@api_view(['GET'])
def popular(request):
    movies = Movie.objects.all().order_by('-popularity')[:30]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@extend_schema(responses=MovieListSerializer)
@api_view(['GET'])
def newMovie(request, page):
    movies = Movie.objects.all().order_by('-release_date')[(page-1) * 30:30*page]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@extend_schema(responses=MovieSearchSerializer)
@api_view(['GET'])
def search(request, title):
    movies = Movie.objects.filter(title__contains=title)
    serializer = MovieSearchSerializer(movies, many=True)
    return Response(serializer.data)


@extend_schema(responses=MovieListSerializer)
@api_view(['GET'])
def detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    serializer = MovieListSerializer(movie)

    reviews = movie.review_set.all()
    reviews_cnt = len(reviews)
    reviews_sum = 0

    for review in reviews:
        reviews_sum += review.sentiment

    reviews_avg = 0

    if reviews_cnt:
        reviews_avg = round(reviews_sum / reviews_cnt)

    data = {
        'movies': serializer.data,
        'reviews_avg': reviews_avg,
    }

    print(data)

    return Response(data)


@extend_schema(responses=MovieListSerializer)
@api_view(['GET'])
def genre(request, genre, page):
    genre = get_object_or_404(Genre, name=genre)
    movies = Movie.objects.filter(genres=genre).all()
    page_cnt = math.ceil(len(movies) / 30)
    movies = movies[(page-1) * 30:30*page]

    serializer = MovieListSerializer(movies, many=True)

    data = {
        'page_cnt': page_cnt,
        'movies': serializer.data,
    }

    return Response(data)


def recommendAnonymous():
    index = [i for i in range(100)]
    movies = Movie.objects.order_by('-popularity', '-release_date', '-vote_average')[:100]
    movie_data = []

    index = random.sample(index, 30)

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
            movies = Movie.objects.filter(genres=genre).order_by(random.sample(rand_filter, 1)[0])[:30]
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


@api_view(['GET'])
def credit(request, movie_id):
    tmdb_api = os.environ.get('TMDB_API')
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={tmdb_api}&language=ko-KR")

    response = response.json()

    return Response(response['cast'])
    

@api_view(['GET'])
def similar(request, movie_id):
    tmdb_api = os.environ.get('TMDB_API')
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}/similar?api_key={tmdb_api}&language=ko-KR&page=1")
    response = response.json()

    return Response(response['results'])


# @api_view(['GET'])
# def tmdb(request):
#     tmdb_api = os.environ.get('TMDB_API')


#     for page in range(1, 1001):
#         response = requests.get(f"https://api.themoviedb.org/3/movie/popular?api_key={tmdb_api}&language=ko-KR&page={page}")
#         response = response.json()

#         for movie in response.get('results'):
#             try:
#                 m = Movie()
#                 m.id = movie['id']
#                 if movie['overview'] == '':
#                     continue
#                 m.overview = movie['overview']

#                 m.release_date = movie['release_date']
#                 m.title = movie['title']
#                 if not movie['backdrop_path']:
#                     continue
                
#                 m.backdrop_path = 'https://image.tmdb.org/t/p/w500' + movie['backdrop_path']
#                 m.popularity = movie['popularity']
#                 m.vote_count = movie['vote_count']

#                 if movie['vote_average'] == 0:
#                     continue

#                 m.vote_average = movie['vote_average']
#                 m.poster_path = 'https://image.tmdb.org/t/p/w200' + movie['poster_path']
#                 m.save()

#                 for genre in movie['genre_ids']:
#                     genre = get_object_or_404(Genre, id=genre)
#                     m.genres.add(genre)
#             except(Exception):
#                 continue

#         print(page)