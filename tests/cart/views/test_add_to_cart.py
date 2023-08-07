from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from bakeryProject.cart.models import Product, CartItem, Cart

User = get_user_model()


class AddToCartViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@test.com', password='testpass123456')
        self.cart = Cart.objects.create(user=self.user)
        self.product = Product.objects.create(name='Test Product', price=10.00)
        self.client.login(username='testuser@test.com', password='testpass123456')
        self.url = reverse('add_to_cart')

    def test_add_to_cart__adding_new_product_success(self):
        data = {'product': self.product.id, 'quantity': 1}
        referer_url = reverse('products_list')
        response = self.client.post(self.url, data=data, HTTP_REFERER=referer_url)

        # Check success redirect
        self.assertEqual(response.status_code, 302)

        cart_item = CartItem.objects.filter(cart=self.user.cart, product=self.product).first()

        # Check the existence of the cart item
        self.assertTrue(cart_item)

        # Check the quantity of the cart item
        self.assertEqual(cart_item.quantity, 1)

        redirect_url = reverse('products_list') + f"#product-{self.product.pk}"

        # Check correct page to redirect
        self.assertRedirects(response, redirect_url)

    def test_add_to_cart__adding_quantity_to_existing_item_success(self):
        referer_url = reverse('products_list')
        existing_item = CartItem.objects.create(cart=self.user.cart, product=self.product, quantity=1)
        response = self.client.post(self.url, data={'product': self.product.id, 'quantity': 3}, HTTP_REFERER=referer_url, follow=True)
        self.assertEqual(response.status_code, 200)

        existing_item.refresh_from_db()
        self.assertEqual(existing_item.quantity, 4)

    def test_unauthenticated_user_access(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
