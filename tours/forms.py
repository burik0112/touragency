from django import forms

from django import forms
from tours.models import OrderModel


class OrderModelForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        exclude = ['created_at']