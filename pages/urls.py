from django.urls import path

from pages.views import HomeView, DestinationView, DestinationDetailView, BlogView, BlogDetailView, ContactView, \
    AboutView

app_name = 'pages'

urlpatterns = [
    path('blog/', BlogView.as_view(), name='blog'),
    path('blogdetail/', BlogDetailView.as_view(), name='blogdetail'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('', HomeView.as_view(), name='home'),
]