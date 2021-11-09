from django.contrib import admin

from posts.models import PostTagModel, PostModel, CommentModel


@admin.register(PostTagModel)
class PostTagModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', ]
    list_filter = ['created_at', 'tags']
    autocomplete_fields = ['tags']


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['phone', 'created_at', 'name', 'email', 'comment']
    list_filter = ['created_at', 'phone']
    search_fields = ['name']
