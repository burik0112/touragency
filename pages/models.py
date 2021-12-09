from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactModel(models.Model):
    name = models.CharField(max_length=20, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    message = models.TextField(max_length=225, verbose_name=_('message'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')


class HomeModel(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)
    place = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'home'
        verbose_name_plural = 'homes'


class PlaceModel(models.Model):
    title = models.TextField(max_length=40)
    img = models.ImageField(upload_to='images')
    price = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'place'
        verbose_name_plural = 'places'


class TripModel(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='img')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'trip'
        verbose_name_plural = 'trips'
