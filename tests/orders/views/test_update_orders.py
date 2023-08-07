from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from bakeryProject.orders.models import Order

User = get_user_model()


class UpdateOrderViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@test.com', password='testpassword12345')
        self.client.login(email='testuser@test.com', password='testpassword12345')
        self.order1 = Order.objects.create(user=self.user, status='received', pickup_time=timezone.now(),
                                           total_price=10)
        self.order2 = Order.objects.create(user=self.user, status='working', pickup_time=timezone.now(),
                                           total_price=10)
        self.order3 = Order.objects.create(user=self.user, status='ready_to_pickup', pickup_time=timezone.now(),
                                           total_price=10)

    def test_update_order_view_authenticated_user(self):
        self.update_order_url = reverse('update_order', args=[self.order1.pk])
        response = self.client.post(self.update_order_url)
        self.assertEqual(response.status_code, 302)
        updated_order = Order.objects.get(pk=self.order1.pk)
        self.assertNotEqual(updated_order.status, 'received')
        self.assertRedirects(response, reverse('show_orders'))

    def test_update_order__changing_status_to_working(self):
        self.update_order_url = reverse('update_order', args=[self.order1.pk])
        self.client.post(self.update_order_url)
        updated_order = Order.objects.get(pk=self.order1.pk)
        self.assertEqual(updated_order.status, 'working')
        # self.assertEqual(updated_order.status, 'done')

    def test_update_order__changing_status_to_ready_to_pickup(self):
        self.update_order_url = reverse('update_order', args=[self.order2.pk])
        self.client.post(self.update_order_url)
        updated_order = Order.objects.get(pk=self.order2.pk)
        self.assertEqual(updated_order.status, 'ready_to_pickup')

    def test_update_order__changing_status_to_done(self):
        self.update_order_url = reverse('update_order', args=[self.order3.pk])
        self.client.post(self.update_order_url)
        updated_order = Order.objects.get(pk=self.order3.pk)
        self.assertEqual(updated_order.status, 'done')
