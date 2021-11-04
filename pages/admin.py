from django.contrib import admin

from pages.models import ContactModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'message']
