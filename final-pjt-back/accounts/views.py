from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

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