from django.contrib.auth import authenticate
from django.test import TestCase, RequestFactory, Client

# Create your tests here.
from django.urls import reverse

from users.models import CustomUser


class UserTestCase(TestCase):
    def test_authenticate(self):
        test_user = CustomUser._default_manager.create_user(
            uname='test',
            email='test@example.com',
            password='test',
        )
        authenticated_user = authenticate(uname='test', password='test')
        self.assertEqual(test_user, authenticated_user)
