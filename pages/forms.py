from django import forms

from pages.models import ContactModel, OrderModel


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        exclude = ['created_at']


class OrderModelForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        exclude = ['created_at']
