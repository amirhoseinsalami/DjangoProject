# accounts/tests.py
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class AccountsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass123')

    # --- Registration ---
    def test_register_page_loads(self):
        response = self.client.get(reverse('accounts:register'))
        self.assertEqual(response.status_code, 200)

    def test_register_creates_user(self):
        self.client.post(reverse('accounts:register'), {
            'username': 'newuser',
            'password1': 'complexpass123!',
            'password2': 'complexpass123!',
        })
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_register_redirects_after_success(self):
        response = self.client.post(reverse('accounts:register'), {
            'username': 'newuser2',
            'password1': 'complexpass123!',
            'password2': 'complexpass123!',
        })
        self.assertEqual(response.status_code, 302)

    # --- Login / Logout ---
    def test_login_valid(self):
        response = self.client.post(reverse('accounts:login'), {
            'username': 'testuser',
            'password': 'testpass123',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_invalid(self):
        response = self.client.post(reverse('accounts:login'), {
            'username': 'testuser',
            'password': 'wrongpass',
        })
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_logout(self):
        self.client.login(username='testuser', password='testpass123')
        self.client.post(reverse('accounts:logout'))
        response = self.client.get(reverse('accounts:profile'))
        self.assertNotEqual(response.status_code, 200)  # redirected away

    # --- Profile ---
    def test_profile_requires_login(self):
        response = self.client.get(reverse('accounts:profile'))
        self.assertEqual(response.status_code, 302)

    def test_profile_loads_for_authenticated(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('accounts:profile'))
        self.assertEqual(response.status_code, 200)

    # --- Profile Update ---
    def test_profile_update_username(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('accounts:profile_edit'), {
            'username': 'updateduser',
            'date_joined': self.user.date_joined.strftime('%Y-%m-%d %H:%M:%S'),
        })
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updateduser')

    def test_delete_photo_resets_avatar(self):
        self.client.login(username='testuser', password='testpass123')
        self.client.post(reverse('accounts:change_photo'), {
            'username': 'testuser',
            'delete_photo': 'true',
        })
        self.user.refresh_from_db()
        self.assertEqual(self.user.profile.photo.name, 'profiles/default.png')
