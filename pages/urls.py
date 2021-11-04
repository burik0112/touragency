from django.urls import path

from pages.views import HomeView, DestinationView, DestinationDetailView, BlogView, BlogDetailView, ContactView, \
    AboutView

app_name = 'pages'

urlpatterns = [
    path('destination/', DestinationView.as_view(), name='destination'),
    path('destinationdetail/', DestinationDetailView.as_view(), name='destinationdetail'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blogdetail/', BlogDetailView.as_view(), name='blogdetail'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('', HomeView.as_view(), name='home'),
]