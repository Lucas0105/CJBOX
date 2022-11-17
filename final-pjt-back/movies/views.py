from .serializers import MoviePopularListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie

@api_view(['GET'])
def popular(request):
    movies = Movie.objects.all().order_by('-popularity')[:15]
    serializer = MoviePopularListSerializer(movies, many=True)
    print(movies)
    return Response(serializer.data)
