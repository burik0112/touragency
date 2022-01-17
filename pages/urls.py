# from django.contrib.auth.views import LoginView
from django.urls import path

from pages.views import HomeView, AboutView, LoginView, RegisterView, OrderView, order, contact

app_name = 'pages'

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('order/', order, name='order'),
]