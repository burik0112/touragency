from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class TourModel(models.Model):
    # id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    long_description = RichTextUploadingField(verbose_name='long_description', default=0)
    img1 = models.ImageField(upload_to='images')
    price = models.IntegerField(default=0)
    discount = models.PositiveIntegerField(default=0, null=True)
    available = models.BooleanField('В наличии')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'tour'
        verbose_name_plural = 'tours'

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
