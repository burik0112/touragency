from django.urls import path

from api.views import TourListAPIView, TourRetrieveAPIView, TourHotelListAPIView, ApplicationListAPIView, ApplicationCreateAPIView

app_name = 'api'




urlpatterns = [
    path('destinations/', TourListAPIView.as_view(), name='destinations'),
    path('hotels/', TourHotelListAPIView.as_view(), name='hotels'),
    path('application/', ApplicationListAPIView.as_view(), name='application'),
    path('application/create/', ApplicationCreateAPIView.as_view(), name='application'),
    path('destinations/<int:pk>/', TourRetrieveAPIView.as_view(), name='destination'),

]