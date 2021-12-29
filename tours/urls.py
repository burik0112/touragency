from django.urls import path

from tours.views import DestinationsListView, InputListView, PostDestinationDetailView

app_name = 'destinations'

urlpatterns = [
    path('<int:pk>/', PostDestinationDetailView.as_view(), name='detail'),
    path('request/', InputListView.as_view(), name='input'),
    path('destinations/', DestinationsListView.as_view(), name='list'),
]
