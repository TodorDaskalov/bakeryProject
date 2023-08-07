from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class UserCreationViewTestCase(TestCase):
    def setUp(self):
        self.register_url = reverse('user_register')
        self.valid_data = {
            'email': 'test@example.com',
            'password1': 'test12345',
            'password2': 'test12345',
        }

    def test_user_create__success(self):
        response = self.client.post(self.register_url, data=self.valid_data, follow=True)
        self.assertEqual(response.status_code, 200)
        user = User.objects.get(email=self.valid_data['email'])
        self.assertTrue(user)

    def test_user_create__successfully_created_cart(self):
        self.client.post(self.register_url, data=self.valid_data, follow=True)
        user = User.objects.get(email=self.valid_data['email'])
        self.assertTrue(user.cart)

    def test_user_create__successfully_created_profile(self):
        self.client.post(self.register_url, data=self.valid_data, follow=True)
        user = User.objects.get(email=self.valid_data['email'])
        self.assertTrue(user.profile)

    def test_user_create__successfully_redirects_home_page(self):
        response = self.client.post(self.register_url, data=self.valid_data, follow=True)
        self.assertRedirects(response, reverse('home_page'))

    def test_user_create__successfully_login_after_registration(self):
        self.client.post(self.register_url, data=self.valid_data, follow=True)
        user = User.objects.get(email=self.valid_data['email'])
        self.assertEqual(self.client.session['_auth_user_id'], str(user.id))
