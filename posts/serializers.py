from rest_framework import serializers
from .models import Post, PostImage, Like, Comment


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['id', 'image', 'uploaded_at']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'created_at']


class PostSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(many=True, read_only=True)
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'images', 'likes_count', 'comments', 'created_at', 'updated_at']
