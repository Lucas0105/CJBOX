from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404


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