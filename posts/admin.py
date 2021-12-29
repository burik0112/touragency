from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from posts.models import PostTagModel, PostModel, CommentModel


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


@admin.register(PostTagModel)
class PostTagModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(PostModel)
class PostModelAdmin(MyTranslationAdmin):
    list_display = ['id', 'title', 'created_at']
    list_filter = ['created_at', 'tags']
    autocomplete_fields = ['tags']


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['phone', 'created_at', 'name', 'email', 'comment']
    list_filter = ['created_at', 'phone']
    search_fields = ['name']
