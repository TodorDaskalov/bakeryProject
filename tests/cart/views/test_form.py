from django.test import TestCase
from django.utils.datetime_safe import datetime

from bakeryProject.cart.forms import OrderForm


class OrderFormTestCase(TestCase):
    def test_form__pickup_time_required(self):
        form = OrderForm(data={'pickup_time': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('pickup_time', form.errors)
        self.assertEqual(form.errors['pickup_time'][0], 'Please select a pickup time.')

    def test_form__pickup_time_now_not_in_range_of_working_time(self):
        current_time = datetime.now().time()
        form = OrderForm(data={'pickup_time': 'now'})

        if (current_time < datetime.strptime('09:00', '%H:%M').time() or
                current_time > datetime.strptime('19:50', '%H:%M').time()):
            self.assertFalse(form.is_valid())
        else:
            self.assertTrue(form.is_valid())

    def test_form__pickup_time_after_current_time(self):
        current_time = datetime.now().time()
        form = OrderForm(data={'pickup_time': f'{9}:{30}'})
        if current_time >= datetime.strptime('09:30', '%H:%M').time():
            self.assertFalse(form.is_valid())
        else:
            self.assertTrue(form.is_valid())

