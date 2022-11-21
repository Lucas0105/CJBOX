from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.db import transaction
from django.core.files.storage import default_storage
from django.contrib.auth import get_user_model

class UserNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('nickname',)


class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField()
    intro = serializers.CharField(required=False)
    my_image = serializers.ImageField(required=False)

    # Define transaction.atomic to rollback the save operation in case of error
    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.nickname = self.data.get('nickname')
        user.intro = self.data.get('intro')

        if request.FILES:
            path = default_storage.save(f"images/{user}/{request.FILES.get('my_image')}", request.FILES.get('my_image'))
            user.my_image = path

        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('nickname', 'email', 'intro', 'my_image')


class UserStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('nickname', 'my_image')
