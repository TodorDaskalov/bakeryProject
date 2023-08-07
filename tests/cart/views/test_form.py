from django.test import TestCase
from django.utils import timezone
from bakeryProject.cart.forms import OrderForm


class OrderFormTestCase(TestCase):
    def test_form__pickup_time_required(self):
        form = OrderForm(data={'pickup_time': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('pickup_time', form.errors)
        self.assertEqual(form.errors['pickup_time'][0], 'Please select a pickup time.')

    # Test passing only if current time it is not in range of working time of the bakery
    def test_form__pickup_time_now_not_in_range_of_working_time(self):
        form = OrderForm(data={'pickup_time': 'now'})
        self.assertFalse(form.is_valid())
        self.assertIn('pickup_time', form.errors)
        self.assertEqual(form.errors['pickup_time'][0], 'Pickup time should be between 9:00 and 20:00.')

    # Test passing only if current time is after 09:00
    def test_form__pickup_time_after_current_time(self):
        now = timezone.now().time()
        form = OrderForm(data={'pickup_time': '09:00'})
        self.assertFalse(form.is_valid())
        self.assertIn('pickup_time', form.errors)
        self.assertEqual(form.errors['pickup_time'][0], 'Pickup time should be after the current time.')
