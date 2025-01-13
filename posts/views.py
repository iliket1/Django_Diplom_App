from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Post, Like, Comment
from .serializers import PostSerializer, CommentSerializer
from .forms import PostForm, CommentForm

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        post_id = self.request.data.get('post')
        serializer.save(user=self.request.user, post_id=post_id)

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post-list')
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form})

class LikeCreateView(generics.GenericAPIView):
    queryset = Like.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        post_id = self.kwargs.get('post_id')
        like, created = Like.objects.get_or_create(user=request.user, post_id=post_id)
        if not created:
            like.delete()
            return Response({'detail': 'Like removed.'}, status=status.HTTP_200_OK)
        return Response ({'detail': 'Like added.'}, status=status.HTTP_201_CREATED)

