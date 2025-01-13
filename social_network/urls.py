"""
URL configuration for social_network project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from posts.views import PostListCreateView, CommentCreateView, LikeCreateView, post_list, post_create
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('api/comments/', CommentCreateView.as_view(), name='comment-create'),
    path('api/posts/<int:post_id>/like/', LikeCreateView.as_view(), name='post-like'),
    path('', post_list, name='post-list'),
    path('create/', post_create, name='post-create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

