from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from movies.models import Movie
from .models import Review, Comment
from django.shortcuts import get_object_or_404
from .serializers import ReviewListSerializer, CommentSerializer
import math


# Create your views here.
@api_view(['POST', 'PUT', 'DELETE'])
def review(request):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, id=request.data.get('movie_id'))
        user = request.user
        serializer = ReviewListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    elif request.method == 'PUT':
        review = get_object_or_404(Review, id=request.data.get('review_id'))
        serializer = ReviewListSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    elif request.method == 'DELETE':
        review = get_object_or_404(Review, id=request.data.get('review_id'))

        if review.user == request.user:
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


@extend_schema(responses=ReviewListSerializer)
@api_view(['GET'])
def reviewRead(request, movie_id, page):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = movie.review_set.all()
    page_cnt = math.ceil(len(reviews) / 5)
    reviews = reviews[(page-1)*5:page*5]

    serializer = ReviewListSerializer(reviews, many=True)

    data = {
        'reviews': serializer.data,
        'page_cnt': page_cnt
    }
    return Response(data)


@extend_schema(responses=ReviewListSerializer)
@api_view(['GET'])
def detail(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    serializer = ReviewListSerializer(review)
    return Response(serializer.data)


@api_view(['POST'])
def commentCreate(request):
    review = get_object_or_404(Review, id=request.data.get('review_id'))
    user = request.user

    serializer = CommentSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review, user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    