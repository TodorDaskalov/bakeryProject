from datetime import datetime
from django import forms


class OrderForm(forms.Form):
    NOW_OPTION = [('now', 'Now')]
    TIME_INTERVALS = [(f'{hour:02d}:{minute:02d}', f'{hour:02d}:{minute:02d}') for hour in range(9, 20) for minute in
                      range(0, 60, 10)]

    pickup_time = forms.ChoiceField(choices=NOW_OPTION + TIME_INTERVALS, error_messages=
                                    {'required': 'Please select a pickup time.'})

    def clean_pickup_time(self):
        pickup_time = self.cleaned_data['pickup_time']

        if pickup_time == 'now':
            current_time = datetime.now().strftime('%H:%M')
            pickup_time = current_time

        hour, minute = map(int, pickup_time.split(':'))

        if hour < 9 or hour >= 20:
            raise forms.ValidationError("Pickup time should be between 9:00 and 20:00.")

        current_time = datetime.now().time()
        if hour < current_time.hour or (hour == current_time.hour and minute < current_time.minute):
            raise forms.ValidationError("Pickup time should be after the current time.")

        return pickup_time
