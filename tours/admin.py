from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from tours.models import TourModel, TourTagModel, CityModel, Category, TourHotelModel


class MyTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(TourModel)
class TourModelAdmin(MyTranslationAdmin):
    list_display = ['id', 'title', 'short_description', 'image', 'price', 'discount']
    list_filter = ['price']
    search_fields = ['title', 'discount', 'message', 'created_at']


@admin.register(TourTagModel)
class ProductTagModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(CityModel)
class CityModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(TourHotelModel)
class TourHotelModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_descriptions', 'image', 'category']
    search_fields = ['title', 'category']
    list_filter = ['created_at', 'category']