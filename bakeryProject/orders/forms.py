from django import forms

from bakeryProject.bakery_main.models import Profile


class CustomOrderForm(forms.Form):
    customer_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    order_text = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        user = self.initial.get('user')
        if user and user.email:
            self.fields['email'].initial = user.email

        customer_name = str(Profile.objects.filter(user=user).first())

        customer_name = customer_name.replace('None', '').strip()

        self.fields['customer_name'].initial = customer_name
        self.fields['customer_name'].widget.attrs['placeholder'] = "Please write your name here"
