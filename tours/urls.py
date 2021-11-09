from django.urls import path

from tours.views import DestinationDetailView, DestinationListView

urlpatterns = [
    path('<int:pk>/', DestinationDetailView.as_view(), name='detail'),
    path('destination/', DestinationListView.as_view(), name='list'),
]