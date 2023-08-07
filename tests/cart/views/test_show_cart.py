from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from bakeryProject.cart.models import Cart, CartItem
from bakeryProject.products.models import Product

User = get_user_model()


class CartViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@test.com', password='testpassword12345')
        self.client.login(username='testuser@test.com', password='testpassword12345')
        self.cart = Cart.objects.create(user=self.user)
        self.url = reverse('cart_page')
        self.product = Product.objects.create(name='Test Product', price=10.00)
        self.cart_item = CartItem.objects.create(cart=self.cart, product=self.product, quantity=2)

    def test_cart__correct_cart_items_display(self):
        response = self.client.get(self.url)
        self.assertContains(response, 'Test Product')
        self.assertContains(response, 'Quantity: 2')

    def test_cart__no_cart_items_to_display_display_message(self):
        self.cart.items.all().delete()
        response = self.client.get(self.url)
        self.assertContains(response, 'Your cart is empty.')
