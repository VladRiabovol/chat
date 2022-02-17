from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser
from account.models import Account


class AccountTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.factory = RequestFactory()
        cls.user = Account.objects.create_user(username='admin',
                                               email='admin@admin.com',
                                               password='admin')
        cls.superuser = Account.objects.create_superuser(username='superuser',
                                                         email='superuser@superuser.com',
                                                         password='superuser')

    def test_string_representation(self):
        expect_representation_custom_user = 'admin'
        expect_representation_custom_superuser = 'superuser'
        self.assertEqual(expect_representation_custom_user, self.user.username)
        self.assertEqual(expect_representation_custom_superuser, self.superuser.username)


