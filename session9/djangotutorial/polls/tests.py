from django.test import TestCase
from .models import BlogPost

class BlogPostTestCase(TestCase):
    def test_blogpost_creation(self):
        post = BlogPost.objects.create(title="Test Post", content="Test content")
        self.assertEqual(post.title, "Test Post")
        self.assertEqual(post.content, "Test content")
        self.assertIsNotNone(post.published_date)
