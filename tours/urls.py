from django.urls import path

from tours.views import DestinationsListView, InputListView, DestinationCreateView

app_name = 'destinations'

urlpatterns = [
    path('<int:pk>/', DestinationCreateView.as_view(), name='detail'),
    path('request/', InputListView.as_view(), name='input'),
    path('destinations/', DestinationsListView.as_view(), name='list'),
]
