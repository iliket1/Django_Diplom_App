from rest_framework import serializers
from .models import Post, PostImage, Like, Comment


class PostImageSerializer(serializers.ModelSerializer):
    """Сериализатор для изображений постов."""
    class Meta:
        model = PostImage
        fields = ['id', 'image', 'uploaded_at']

class LikeSerializer(serializers.ModelSerializer):
    """Сериализатор для лайков постов."""
    class Meta:
        model = Like
        fields = ['id', 'user', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для комментариев."""
    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'created_at']


class PostSerializer(serializers.ModelSerializer):
    """
    Сериализатор для постов.

    Дополнительно включает:
    - Список изображений.
    - Количество лайков.
    - Список комментариев.
    """
    images = PostImageSerializer(many=True, read_only=True)
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'images', 'likes_count', 'comments', 'created_at', 'updated_at']
