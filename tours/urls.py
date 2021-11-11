from django.urls import path

from tours.views import DestinationDetailView, DestinationListView

app_name = 'destinations'

urlpatterns = [
    path('<int:pk>/', DestinationDetailView.as_view(), name='detail'),
    path('destinations/', DestinationListView.as_view(), name='list'),
]