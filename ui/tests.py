from django.contrib.auth.models import User
from django.test import TestCase
from django.test import Client
from django.urls import reverse

from .models import Post



class CreatePostTests(TestCase):
    """
    As a logged-in user, I would like to create a post with a
    title, body, and category so that I can have a new post connected
    to my user profile
    """

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='foo')

    def test_login_required(self):
        url = reverse('create-post')
        response = self.client.get(url)
        self.assertEqual(302, response.status_code)

    def test_route_returns_200_when_user_logged_in(self):
        url = reverse('create-post')
        self.client.force_login(self.user)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

    def test_num_posts_increments_by_one_on_post(self):
        url = reverse('create-post')
        self.client.force_login(self.user)

        # Sanity check
        num_posts_before = Post.objects.all().count()
        data = {'title': 'post title', 'body': 'post body',
                'category': 'hobby'}
        self.client.post(url, data)
        num_posts_after = Post.objects.all().count()
        self.assertEqual(num_posts_before + 1, num_posts_after)

    def test_new_post_has_correct_content(self):
        url = reverse('create-post')
        self.client.force_login(self.user)
        data = {'title': 'post title', 'body': 'post body',
                'category': 'hobby'}
        self.client.post(url, data)
        post = Post.objects.first()
        self.assertDictEqual(data, {'title': post.title,
                                    'body': post.body,
                                    'category': post.category})

    def test_successful_post_returns_correct_template(self):
        url = reverse('create-post')
        self.client.force_login(self.user)
        data = {'title': 'post title', 'body': 'post body',
                'category': 'hobby'}
        response = self.client.post(url, data)
        self.assertTemplateUsed(response, 'ui/post.html')

    def test_correct_user_attached_to_post(self):
        url = reverse('create-post')
        self.client.force_login(self.user)
        data = {'title': 'post title', 'body': 'post body',
                'category': 'hobby'}
        self.client.post(url, data)
        post = Post.objects.first()
        self.assertEqual(self.user, post.user)
