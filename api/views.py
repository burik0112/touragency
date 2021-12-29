from rest_framework.generics import ListAPIView, RetrieveAPIView

from api.serializers import TourSerializer
from tours.models import TourModel


class TourListAPIView(ListAPIView):
    serializer_class = TourSerializer
    queryset = TourModel.objects.all()


class TourRetrieveAPIView(RetrieveAPIView):
    serializer_class = TourSerializer
    model = TourModel
    queryset = TourModel.objects.all()
