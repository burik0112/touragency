from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import gettext_lazy as _


class PostTagModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('post tag')
        verbose_name_plural = _('post tags')


class PostModel(models.Model):
    title = models.CharField(max_length=512, verbose_name=_('title'))
    image = models.ImageField(upload_to='posts', verbose_name=_('image'))
    banner = models.ImageField(upload_to='post banners', verbose_name=_('banner'))
    short_description = models.TextField(default=0)

    tags = models.ManyToManyField(PostTagModel,
                                  related_name='posts', verbose_name=_('tags'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def get_comments(self):
        return self.comments.order_by('-created_at')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')


class CommentModel(models.Model):
    name = models.CharField(max_length=30, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('phone'))
    comment = models.TextField(verbose_name=_('comment'))

    post = models.ForeignKey(
        PostModel,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name=_('post')
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
