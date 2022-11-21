from rest_framework import serializers
from .models import Review, Comment
from movies.models import Movie
from accounts.serializers import UserNameSerializer


class ReviewListSerializer(serializers.ModelSerializer):

    user = UserNameSerializer(read_only = True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user', 'movie', 'likes')


class CommentSerializer(serializers.ModelSerializer):

    user = UserNameSerializer(read_only = True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'review')


class ReviewCommentSerializer(serializers.ModelSerializer):

    class MovieSerializesr(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('id', 'title', 'poster_path')


    comment = CommentSerializer(many=True, read_only=True)
    movie = MovieSerializesr(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user', 'movie', 'likes')
