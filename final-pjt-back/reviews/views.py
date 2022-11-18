from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from movies.models import Movie
from django.shortcuts import get_object_or_404
from .serializers import ReviewListSerializer


# Create your views here.
@api_view(['POST'])
def review(request):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, id=request.data.get('movie_id'))
        user = request.user
        serializer = ReviewListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

