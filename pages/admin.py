from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from pages.models import ContactModel, HomeModel, PlaceModel, TripModel, OrderModel


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


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'message']


@admin.register(HomeModel)
class HomeModelAdmin(MyTranslationAdmin):
    list_display = ['id', 'title', 'remains', 'place', 'img', 'created_at']
    search_fields = ['title', 'remains']
    list_filter = ['created_at', 'place', 'remains']


@admin.register(PlaceModel)
class PlaceModelAdmin(MyTranslationAdmin):
    list_display = ['id', 'title', 'img', 'price', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at', 'price']


@admin.register(TripModel)
class TripModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'img', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'messages', 'created_at']
    search_fields = ['name', 'phone_number']
    list_filter = ['created_at', 'name']
