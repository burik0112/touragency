from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class PostTagModel(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post tag'
        verbose_name_plural = 'post tags'


class PostModel(models.Model):
    object = None
    title = models.CharField(max_length=512)
    image = models.ImageField(upload_to='posts')
    banner = models.ImageField(upload_to='post banners')

    tags = models.ManyToManyField(PostTagModel,
                                  related_name='posts')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = "-id",


class CommentModel(models.Model):
    name = models.CharField(max_length=30, verbose_name='name')
    email = models.EmailField(verbose_name='email')
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='phone')
    comment = models.TextField(verbose_name='comment')

    post = models.ForeignKey(
        PostModel,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='post'
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
