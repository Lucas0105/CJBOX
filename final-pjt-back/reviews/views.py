from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from movies.models import Movie
from .models import Review, Comment
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
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

        
@api_view(['POST'])
def like(request):

    if request.user.is_authenticated:
        me = request.user
        review = get_object_or_404(Review, id=request.data.get('review_id'))
        if me != review.user:
            if review.likes.filter(id=me.id).exists():
                review.likes.remove(me)
                can_review = True
            else :
                review.likes.add(me)
                can_review = False

            data = {
                'like_cnt' : review.likes.count(),
                'can_review': can_review
            }

            return Response(data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_401_UNAUTHORIZED)


@extend_schema(responses=ReviewListSerializer)
@api_view(['GET'])
def reviewRead(request, movie_id, page):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = movie.review_set.order_by('-created_at').all()
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


@extend_schema(responses=CommentSerializer)
@api_view(['GET'])
def commentRead(request, review_id, page):
    review = get_object_or_404(Review, id=review_id)
    comments = review.comment.order_by('-created_at').all()
    page_cnt = math.ceil(len(comments) / 5)
    comments = comments[(page-1)*5 : page*5]

    serializer = CommentSerializer(comments, many=True)

    data = {
        'comments': serializer.data,
        'page_cnt': page_cnt,
    }

    return Response(data)


@api_view(['DELETE'])
def commentDelete(request):
    comment = get_object_or_404(Comment, id=request.data.get('comment_id'))

    if comment.user == request.user:
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)