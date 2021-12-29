from django.urls import reverse
from django.views.generic import ListView, CreateView

from orders.forms import OrderModelForm
from orders.models import OrderModel


# class OrderCreateView(CreateView):
#     template_name = 'orders.html'
#     form_class = OrderModelForm
#
#     def get_success_url(self):
#         return reverse('orders:order')
