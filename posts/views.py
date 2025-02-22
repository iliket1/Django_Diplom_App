from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Post, Like, Comment
from .serializers import PostSerializer, CommentSerializer
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

class PostListCreateView(generics.ListCreateAPIView):
    """
    API-вью для просмотра и создания постов.
    Авторизованные пользователи могут создавать посты.
    """
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Сохраняет пост, добавляя текущего пользователя в качестве автора"""
        serializer.save(author=self.request.user)

class CommentCreateView(generics.CreateAPIView):
    """
    API-вью для создания комментариев.
    Только авторизованные пользователи могут оставлять комментарии.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Сохраняет комментарий, привязывая его к посту и пользователю"""
        post_id = self.request.data.get('post')
        serializer.save(user=self.request.user, post_id=post_id)

@login_required
def post_list(request):
    """
    Представление для отображения списка постов.
    """
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})

@login_required
def post_create(request):
    """
    Представление для создания нового поста.
    Только авторизованные пользователи могут создавать посты.
    """
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user    # Теперь request.user гарантированно не будет анонимным
            post.save()
            return redirect('post-list')
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form})

class LikeCreateView(generics.GenericAPIView):
    """
    API-вью для лайков.
    Позволяет авторизованным пользователям ставить и убирать лайки.
    """
    queryset = Like.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        """Добавляет или удаляет лайк у поста"""
        post_id = self.kwargs.get('post_id')
        like, created = Like.objects.get_or_create(user=request.user, post_id=post_id)
        if not created:
            like.delete()
            return Response({'detail': 'Like removed.'}, status=status.HTTP_200_OK)
        return Response ({'detail': 'Like added.'}, status=status.HTTP_201_CREATED)

