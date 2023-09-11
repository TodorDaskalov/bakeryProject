from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone
from django.utils.datetime_safe import datetime

from bakeryProject.cart.forms import OrderForm


class OrderFormTestCase(TestCase):
    def test_form__pickup_time_required(self):
        form = OrderForm(data={'pickup_time': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('pickup_time', form.errors)
        self.assertEqual(form.errors['pickup_time'][0], 'Please select a pickup time.')

    # Test passing only if current time it is not in range of working time of the bakery
    def test_form__pickup_time_now_not_in_range_of_working_time(self):
        current_time = datetime.now().time()
        form = OrderForm(data={'pickup_time': '10:00'})

        if current_time >= datetime.strptime('09:00', '%H:%M').time():
            # Current time is after 09:00, expect a validation error
            with self.assertRaises(ValidationError):
                form.is_valid()
        else:
            # Current time is before 09:00, form should not have errors
            self.assertTrue(form.is_valid())

    def test_form__pickup_time_after_current_time(self):
        current_time = datetime.now().time()
        form = OrderForm(data={'pickup_time': '09:00'})
        if current_time >= datetime.strptime('09:00', '%H:%M').time():
            # Current time is after 09:00, expect a validation error
            with self.assertRaises(ValidationError):
                form.is_valid()
        else:
            # Current time is before 09:00, form should not have errors
            self.assertTrue(form.is_valid())
