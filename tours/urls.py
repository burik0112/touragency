from django.urls import path

from tours.views import DestinationDetailView, DestinationsListView, InputListView

app_name = 'destinations'

urlpatterns = [
    path('<int:pk>/', DestinationDetailView.as_view(), name='detail'),
    path('request/', InputListView.as_view(), name='input'),
    path('destinations/', DestinationsListView.as_view(), name='list'),
]
