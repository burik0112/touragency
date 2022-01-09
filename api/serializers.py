from abc import ABC

from rest_framework import serializers

from tours.models import TourModel, TourTagModel, TourHotelModel


class TourTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourTagModel
        fields = '__all__'


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourModel
        fields = '__all__'
# exclude = [
        #     'title_ru', 'title_en', 'image', 'price_ru', 'price_en',
        #     'short_description_en', 'short_description_ru',
        # ]


class TourHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourHotelModel
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourHotelModel
        fields = '__all__'
