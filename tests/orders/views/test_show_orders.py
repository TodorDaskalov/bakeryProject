from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from bakeryProject.orders.models import Order
from django.utils import timezone

User = get_user_model()

# Test passing in working time of the bakery


class ShowOrdersViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@test.com', password='testpassword12345')
        self.client.login(username='testuser@test.com', password='testpassword12345')
        self.orders_url = reverse('show_orders')
        self.order1 = Order.objects.create(user=self.user, status='received', pickup_time=timezone.now(), total_price=10)
        self.order2 = Order.objects.create(user=self.user, status='working', pickup_time=timezone.now(), total_price=10)
        self.order3 = Order.objects.create(user=self.user, status='ready_to_pickup', pickup_time=timezone.now(), total_price=10)
        self.order4 = Order.objects.create(user=self.user, status='Done', pickup_time=timezone.now(), total_price=10)

    def test_show_orders__correct_orders_count_and_type(self):
        response = self.client.get(self.orders_url)
        self.assertEqual(len(response.context['orders']), 3)
        self.assertEqual(len(response.context['received_orders']), 1)
        self.assertEqual(len(response.context['working_on_it_orders']), 1)
        self.assertEqual(len(response.context['ready_orders']), 1)
