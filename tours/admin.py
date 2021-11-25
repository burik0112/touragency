from django.contrib import admin

from tours.models import TourModel, TourTagModel, CityModel


@admin.register(TourModel)
class TourModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'long_description', 'image', 'price', 'discount']
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

#
# @admin.register(CategoryModel)
# class CategoryModelAdmin(admin.ModelAdmin):
#     list_display = ['title', 'created_at']
#     search_fields = ['title']
#     list_filter = ['created_at']
