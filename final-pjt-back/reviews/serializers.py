from rest_framework import serializers
from .models import Review, Comment
from movies.models import Movie


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user', 'movie', 'likes')


class CommentSerializer(serializers.ModelSerializer):

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
