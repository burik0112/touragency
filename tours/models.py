from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import gettext_lazy as _


class TourTagModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('tour tag')
        verbose_name_plural = _('tour tags')


class CityModel(models.Model):
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'city'
        verbose_name_plural = 'cities'


class Category(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class TourModel(models.Model):
    # id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30, verbose_name=_('title'))
    long_description = RichTextUploadingField(verbose_name=_('long_description'), default=0)
    image = models.ImageField(upload_to='images', verbose_name=_('image'))
    price = models.IntegerField(default=0, verbose_name=_('price'))
    discount = models.PositiveIntegerField(default=0, null=True, verbose_name=_('discount'))
    available = models.BooleanField('В наличии')
    tags = models.ManyToManyField(TourTagModel,
                                  related_name='tours',
                                  verbose_name=_('tags'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('tour')
        verbose_name_plural = _('tours')








