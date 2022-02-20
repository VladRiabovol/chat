from django.test import TestCase
from account.models import Account
from account.forms import RegistrationForm


class SignInFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = Account.objects.create_user(username='admin',
                                               email='admin@admin.com',
                                               password='admin')
        cls.superuser = Account.objects.create_superuser(username='superuser',
                                                         email='superuser@superuser.com',
                                                         password='superuser')

    def test_signup_form(self):
        form_data = {
            'email': 'John@john.com',
            'username': 'John',
            'password1': 'password101',
            'password2': 'password101'
        }
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.clean_username(), 'john')
        self.assertEqual(form.clean_email(), 'john@john.com')

    def test_signup_form_exceptions(self):
        form_exception_data = {
            'email': 'admin@admin.com',
            'username': 'admin',
            'password1': 'password101',
            'password2': 'password101'
        }
        form = RegistrationForm(data=form_exception_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'][0], 'Email admin@admin.com is already in use')
        self.assertEqual(form.errors['username'][0], 'Username admin is already in use')

