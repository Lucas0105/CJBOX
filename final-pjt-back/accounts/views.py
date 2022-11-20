from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from movies.models import Movie
from movies.serializers import MovieListSerializer
from reviews.serializers import ReviewListSerializer, ReviewCommentSerializer
import math


@extend_schema(responses=UserSerializer)
@api_view(['GET'])
def my_profile(request, nickname):
    user = request.user
    serializer = UserSerializer(user)
    genres = user.likeGenres.all()

    data = {
        'user' : serializer.data,
        'genres' : genres,
        'followed_cnt' : user.followed.count(),
        'following_cnt' : user.friends.count(),
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

    if user.my_lists.filter(id=movie.id).exists():
        user.my_lists.remove(movie)
    else:
        user.my_lists.add(movie)

    return Response(status=status.HTTP_201_CREATED)


@extend_schema(responses=MovieListSerializer)
@api_view(['GET'])
def myListShow(request, nickname, page):
    User = get_user_model()

    user = get_object_or_404(User, nickname=nickname)

    myList = user.my_lists.all()

    serializer = MovieListSerializer(myList, many=True)

    return Response(serializer.data)


@extend_schema(responses=ReviewCommentSerializer)
@api_view(['GET'])
def review(request, page):
    user = request.user

    reviews = user.review_set.all()
    page_cnt = math.ceil(len(reviews) / 5)
    reviews = user.review_set.all()[(page-1)*5:page*5]

    serializer = ReviewCommentSerializer(reviews, many=True)

    data = {
        'reviews': serializer.data,
        'page_cnt': page_cnt,
    }

    return Response(data)