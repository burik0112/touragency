from datetime import datetime

import pytz

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

    def is_discount(self):
        return self.is_discount != 0

    def get_price(self):
        if self.is_discount():
            return self.price - self.price * self.discount / 100
        return self.price

    def is_new(self):
        diff = datetime.now(pytz.timezone('Asia/Tashkent')) - self.created_at
        return diff.days <= 3

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('tour')
        verbose_name_plural = _('tours')


class OrderModel(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'








