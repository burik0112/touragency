from django.urls import path

from api.views import TourListAPIView, TourRetrieveAPIView

app_name = 'api'


urlpatterns = [
    path('destinations/', TourListAPIView.as_view(), name='destinations'),
    path('destinations/<int:pk>/', TourRetrieveAPIView.as_view(), name='destination'),

]