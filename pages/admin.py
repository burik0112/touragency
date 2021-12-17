from django.contrib import admin

from pages.models import ContactModel, HomeModel, PlaceModel, TripModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'message']


@admin.register(HomeModel)
class HomeModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'remains', 'place', 'img', 'created_at']
    search_fields = ['title', 'remains']
    list_filter = ['created_at', 'place', 'remains']


@admin.register(PlaceModel)
class PlaceModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'img', 'price', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at', 'price']


@admin.register(TripModel)
class TripModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'img', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']
