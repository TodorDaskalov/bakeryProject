from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.datetime_safe import datetime

from bakeryProject.cart.models import Cart, CartItem
from bakeryProject.orders.models import Order
from bakeryProject.products.models import Product

User = get_user_model()

# Test for this case passing only in the working time of the Bakery


class OrderProductsViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@test.com',
            password='testpassword12345'
        )
        self.client.login(email='testuser@test.com', password='testpassword12345')
        self.cart = Cart.objects.create(user=self.user)
        self.product_1 = Product.objects.create(name='Product 1', price=10)
        self.product_2 = Product.objects.create(name='Product 2', price=15)
        self.cart_item_1 = CartItem.objects.create(cart=self.cart, product=self.product_1, quantity=2)
        self.cart_item_2 = CartItem.objects.create(cart=self.cart, product=self.product_2, quantity=3)
        self.url = reverse('order_products')

    def test_order_products__success(self):
        current_time = datetime.now()

        pickup_time = datetime.now().replace(hour=10, minute=0)

        if current_time >= pickup_time:
            # Raise a ValidationError if the pickup time is not valid
            with self.assertRaises(ValidationError):
                self.client.post(self.url, {'pickup_time': '10:00'})
        else:
            # If the current time is before 10:00, the order should be successful
            response = self.client.post(self.url, {'pickup_time': '10:00'})
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'cart/place_order_success.html')
            self.assertEqual(self.cart.items.count(), 0)

    def test_order_products__order_generated_correct_working_custom_filter(self):
        current_time = datetime.now()

        pickup_time = datetime.now().replace(hour=10, minute=0)

        if current_time >= pickup_time:
            # Raise a ValidationError if the pickup time is not valid
            with self.assertRaises(ValidationError):
                self.client.post(self.url, {'pickup_time': '10:00'})
        else:
            # If the current time is before 10:00, the order should be successful
            response = self.client.post(self.url, {'pickup_time': '10:00'})
            self.assertEqual(response.status_code, 200)

            # Check that the expected template is used
            self.assertTemplateUsed(response, 'cart/place_order_success.html')

            # Check that the cart is empty after placing the order
            self.assertEqual(self.cart.items.count(), 0)

            # Check that a new order has been created with the correct details
            order = Order.objects.last()
            self.assertEqual(order.user, self.user)
            self.assertEqual(order.products, 'Product 1 x 2, Product 2 x 3')
            self.assertEqual(order.status, 'received')
            self.assertEqual(order.total_price, 65)

