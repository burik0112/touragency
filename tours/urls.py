from django.urls import path

from tours.views import DestinationDetailView, DestinationsListView

app_name = 'destinations'

urlpatterns = [
    path('<int:pk>/', DestinationDetailView.as_view(), name='detail'),
    path('destinations/', DestinationsListView.as_view(), name='list'),
]