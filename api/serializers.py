from abc import ABC

from rest_framework import serializers

from tours.models import TourModel, TourTagModel


class TourTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourTagModel
        fields = '__all__'


class TourSerializer(serializers.ModelSerializer):

    class Meta:
        model = TourModel
        exclude = ['long_description_ru', 'long_description_en', 'long_description_uz',
                   'title_ru', 'title_en', 'title_uz', 'image', 'price_ru', 'price_en', 'price_uz']
