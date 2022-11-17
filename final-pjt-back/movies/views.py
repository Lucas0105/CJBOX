from .serializers import MovieListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie

@api_view(['GET'])
def popular(request):
    movies = Movie.objects.all().order_by('-popularity')[:15]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def newMovie(request, page):
    movies = Movie.objects.all().order_by('-release_date')[(page-1) * 9:9*page]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

