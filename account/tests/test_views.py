from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import AnonymousUser

from account.models import Account
from account.views import register_view


class PersonalTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.factory = RequestFactory()
        cls.client = Client()
        cls.user = Account.objects.create_user(username='admin',
                                               email='admin@admin.com',
                                               password='admin')

    def test_register_view(self):

        response = self.client.post(
            '/chat/account/register/',
            {'email': 'test@test.com',
             'username': 'test',
             'password1': 'password101',
             'password2': 'password101'}
        )
        response.user = AnonymousUser()
        self.assertEqual(response.status_code, 302)

    def test_exception_register_view(self):
        request = self.factory.post(
            '/chat/account/register/',
            {'email': 'admin@admin.com',
             'username': 'admin',
             'password1': 'password101',
             'password2': 'password101'}
        )
        request.user = self.user
        response = register_view(request)

        self.assertEqual(response.status_code, 200)

