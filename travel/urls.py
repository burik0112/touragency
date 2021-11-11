from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('destinations/', include('tours.urls', namespace='destinations')),
    path('posts/', include('posts.urls', namespace='posts')),
    path('', include('pages.urls')),
]
