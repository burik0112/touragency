from django.db import models


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



