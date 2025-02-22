from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    """
    Модель поста в социальной сети.

    Атрибуты:
    - author: Автор поста (ForeignKey к пользователю).
    - title: Заголовок поста.
    - content: Содержимое поста.
    - created_at: Дата и время создания поста.
    - updated_at: Дата и время последнего обновления.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Возвращает строковое представление поста (его заголовок)."""
        return self.title


class PostImage(models.Model):
    """
    Модель изображения, прикрепленного к посту.

    Атрибуты:
    - post: Пост, к которому прикреплено изображение.
    - image: Файл изображения.
    - uploaded_at: Дата и время загрузки изображения.
    """
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    """
    Модель лайков постов.

    Атрибуты:
    - post: Пост, который лайкнули.
    - user: Пользователь, поставивший лайк.
    - created_at: Дата и время лайка.
    """
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    """
    Модель комментария к посту.

    Атрибуты:
    - post: Пост, к которому оставлен комментарий.
    - user: Автор комментария.
    - text: Текст комментария.
    - created_at: Дата и время создания комментария.
    """
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
