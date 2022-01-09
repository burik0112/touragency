from django.contrib import admin

from orders.models import ApplicationModel


@admin.register(ApplicationModel)
class ApplicationModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'phone', 'created_at']
    search_fields = ['name', 'surname']
    list_filter = ['created_at', 'phone']
