from django import forms

from .models import Order


class CheckoutForms(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone_number', 'address', 'order_nots']
