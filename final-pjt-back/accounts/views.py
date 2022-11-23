from .serializers import UserSerializer, UserStatusSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password
from movies.models import Movie, UserLikeGenres
from reviews.models import Review
from movies.serializers import MovieListSerializer
from reviews.serializers import ReviewCommentSerializer
from .serializers import UserLikeGenresSerializer
import random
import math


@extend_schema(responses=UserSerializer)
@api_view(['GET'])
def my_profile(request, nickname):
    User = get_user_model()
    user = get_object_or_404(User, nickname=nickname)
    serializer = UserSerializer(user)
    genres = UserLikeGenres.objects.filter(user=user).all().order_by('-count')[:5]
    
    genre_serializer = UserLikeGenresSerializer(genres, many=True)

    data = {
        'user' : serializer.data,
        'genres': genre_serializer.data,
        'followed_cnt' : user.followed.count(),
        'following_cnt' : user.friends.count(),
    }

    return Response(data)


@extend_schema(responses=UserStatusSerializer)
@api_view(['GET'])
def userStatus(request):

    if request.user.is_anonymous:
        movies = Movie.objects.order_by('-release_date', '-popularity', '-vote_average').all()[:10]
        index = random.sample([0, 1, 2], 1)
        movie_serializer = MovieListSerializer(movies[index[0]])
        data = {
            'movie': movie_serializer.data,
        }
    else:
        user = request.user
        serializer = UserStatusSerializer(user)
        likeGenres = UserLikeGenres.objects.filter(user=user).all().order_by('-count')[:3]

        index_tmp = [i for i in range(0, len(likeGenres))]

        if index_tmp:
            index = random.sample(index_tmp, 1)

            likeGenre = likeGenres[index[0]]

            movies =  Movie.objects.filter(genres=likeGenre.genre).order_by('-release_date', '-popularity', '-vote_average')[:3]

            index = random.sample([0, 1, 2], 1)
        else:
            movies = Movie.objects.order_by('-release_date', '-popularity', '-vote_average').all()[:10]
            index = random.sample([0, 1, 2], 1)
        movie_serializer = MovieListSerializer(movies[index[0]])

        data = {
            'user': serializer.data,
            'movie': movie_serializer.data,
        }

    return Response(data)


@api_view(['POST'])
def follow(request):
    User = get_user_model()

    me = request.user
    you = get_object_or_404(User, nickname=request.data.get('nickname'))

    if me != you:
        if me.friends.filter(id=you.id).exists():
            me.friends.remove(you)
        else :
            me.friends.add(you)
    
    return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def myList(request):
    user = request.user

    movie = get_object_or_404(Movie, id=request.data.get('movie_id'))
    genres = movie.genres.all()

    if user.my_lists.filter(id=movie.id).exists():
        user.my_lists.remove(movie)
        for genre in genres:
            likeGenres = UserLikeGenres.objects.get(user=user, genre=genre)
            likeGenres.count -= 1
            likeGenres.save()
    else:
        user.my_lists.add(movie)
        for genre in genres:
            likeGenres, _ = UserLikeGenres.objects.get_or_create(user=user, genre=genre)
            likeGenres.count += 1
            likeGenres.save()


    return Response(status=status.HTTP_201_CREATED)


@extend_schema(responses=MovieListSerializer)
@api_view(['GET'])
def myListShow(request, nickname, page):
    User = get_user_model()

    user = get_object_or_404(User, nickname=nickname)

    myList = user.my_lists.all()
    page_cnt = math.ceil(len(myList) / 12)
    myList = myList[(page-1)*12:page*12]
    serializer = MovieListSerializer(myList, many=True)

    data = {
        'myList': serializer.data,
        'page_cnt': page_cnt
    }

    return Response(data)


@extend_schema(responses=ReviewCommentSerializer)
@api_view(['GET'])
def review(request, nickname, page):
    User = get_user_model()

    user = get_object_or_404(User, nickname=nickname)

    reviews = user.review_set.all()
    page_cnt = math.ceil(len(reviews) / 3)
    reviews = reviews[(page-1)*3:page*3]

    serializer = ReviewCommentSerializer(reviews, many=True)

    data = {
        'reviews': serializer.data,
        'page_cnt': page_cnt,
    }

    return Response(data)


@api_view(['POST'])
def kakao(request):
    User = get_user_model()
    data = request.data
    
    if not User.objects.filter(username=data['username']).exists():
        pw = make_password(data['password'])
        user = User(username=data['username'], nickname=data['nickname'], password=pw, my_image=data['my_image'])
        user.save()

    return Response(status=status.HTTP_201_CREATED)
    

