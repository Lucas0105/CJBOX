from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from movies.models import Movie
from .models import Review
from django.shortcuts import get_object_or_404
from .serializers import ReviewListSerializer
import math


# Create your views here.
@api_view(['POST', 'PUT'])
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