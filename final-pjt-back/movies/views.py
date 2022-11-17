from .serializers import MovieListSerializer, MovieSearchSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema
from django.db.models import Q
from .models import Movie


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