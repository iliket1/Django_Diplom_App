from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post, Like, Comment

User = get_user_model()

class PostTestCase(TestCase):
    """Тесты для модели Post, Like и Comment."""

    def setUp(self):
        """
        Создает тестового пользователя и пост перед выполнением тестов.
        """
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(author=self.user, title='Test Post', content='Test Content')

    def test_post_creation(self):
        """Проверяет, что пост создается корректно."""
        self.assertEqual(Post.objects.count(), 1)

    def test_like_post(self):
        """Проверяет, что можно поставить лайк посту."""
        Like.objects.create(user=self.user, post=self.post)
        self.assertEqual(self.post.likes.count(), 1)

    def test_comment_post(self):
        """Проверяет, что можно оставить комментарий к посту."""
        Comment.objects.create(user=self.user, post=self.post, text='Test Comment')
        self.assertEqual(self.post.comments.count(), 1)
