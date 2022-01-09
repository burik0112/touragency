from rest_framework.generics import ListAPIView, RetrieveAPIView

from api.serializers import TourSerializer, TourHotelSerializer, ApplicationSerializer
from orders.models import ApplicationModel
from tours.models import TourModel, TourHotelModel


class TourListAPIView(ListAPIView):
    serializer_class = TourSerializer
    queryset = TourModel.objects.all()


class TourRetrieveAPIView(RetrieveAPIView):
    serializer_class = TourSerializer
    model = TourModel
    queryset = TourModel.objects.all()


class TourHotelListAPIView(ListAPIView):
    serializer_class = TourHotelSerializer
    queryset = TourHotelModel.objects.all()


class ApplicationListAPIView(ListAPIView):
    serializer_class = ApplicationSerializer
    queryset = ApplicationModel.objects.all()
