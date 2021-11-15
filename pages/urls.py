from django.urls import path

from pages.views import HomeView, ContactView, AboutView

app_name = 'pages'

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('', HomeView.as_view(), name='home'),
]