from django.contrib import admin

from tours.models import TourModel


@admin.register(TourModel)
class TourModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'long_description','img1','price','discount']
    list_filter = ['price']
    search_fields = ['title', 'discount', 'message','created_at']
