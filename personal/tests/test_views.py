from django.test import TestCase, Client
from account.models import Account


class PersonalTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = Account.objects.create_user(username='admin',
                                               email='admin@admin.com',
                                               password='admin')

    def test_home_screen_view(self):
        response = self.client.get('/chat/personal/')
        response.user = self.user
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'personal/home.html')