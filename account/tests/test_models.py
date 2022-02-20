from django.test import TestCase
from account.models import Account, get_profile_image_filepath


class AccountTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = Account.objects.create_user(username='admin',
                                               email='admin@admin.com',
                                               password='admin')
        cls.superuser = Account.objects.create_superuser(username='superuser',
                                                         email='superuser@superuser.com',
                                                         password='superuser')

    def test_create_user(self):
        self.assertEqual(self.user.__str__(), 'admin')
        self.assertEqual(self.user.email, 'admin@admin.com')
        self.assertEqual(self.user.USERNAME_FIELD, 'email')
        self.assertTrue(self.user.check_password('admin'))
        self.assertEqual(self.user.is_superuser, False)
        self.assertEqual(self.user.is_admin, False)
        self.assertEqual(self.user.is_staff, False)
        self.assertEqual(self.user.has_perm(self.user), False)
        self.assertEqual(self.user.has_module_perms(app_label='account'), True)

    def test_exceptions_create_user(self):
        with self.assertRaises(ValueError):
            account = Account.objects.create_user(email='',
                                                  username='admin1',
                                                  password='password101')
        with self.assertRaises(ValueError):
            account = Account.objects.create_user(email='admin1',
                                                  username='',
                                                  password='password101')

    def test_create_superuser(self):
        self.assertEqual(self.superuser.__str__(), 'superuser')
        self.assertEqual(self.superuser.email, 'superuser@superuser.com')
        self.assertEqual(self.superuser.USERNAME_FIELD, 'email')
        self.assertTrue(self.superuser.check_password('superuser'))
        self.assertEqual(self.superuser.is_superuser, True)
        self.assertEqual(self.superuser.is_admin, True)
        self.assertEqual(self.superuser.is_staff, True)
        self.assertEqual(self.superuser.has_perm(self.user), True)
        self.assertEqual(self.superuser.has_module_perms(app_label='account'), True)

    def test_get_profile_image_filepath(self):
        self.assertEqual(get_profile_image_filepath(self.user), 'profile_images/3/profile_image.png')





