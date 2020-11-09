from django.test import TestCase
from django.contrib.auth.models import User
from .models import User, Post
# Create your tests here.


class PostsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user1 = User.objects.create_user(username='Beo', password='Wulf')
        user1.save()

        post = Post.objects.create(author=user1, title="Schrodinger's cat",
        body="""This test exists in passed and failed states until you view the test result. 
        So much for determinism huh""")

    def test_post_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'Beo')
        self.assertEqual(title, "Schrodinger's cat")
        self.assertEqual(body, """This test exists in passed and failed states until you view the test result. 
        So much for determinism huh""")

