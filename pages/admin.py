from django.contrib import admin

from pages.models import ContactModel, HomeModel, PlaceModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'message']

@admin.register(HomeModel)
class HomeModelAdmin(admin.ModelAdmin):
    list_display = ['img', 'created_at', 'title', 'place']
    search_fields = ['title', 'place']
    list_filter = ['created_at']


@admin.register(PlaceModel)
class PlaceModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'img', 'price', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at', 'price']