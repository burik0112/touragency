from django.db import models

from tours.models import TourModel
from users.models import UserModel


class OrderModel(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField(null=True)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    postcode = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address1 = models.CharField(max_length=30)
    address2 = models.CharField(max_length=30, null=True, blank=True)

    tours = models.ManyToManyField(TourModel, related_name='orders')
    price = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        UserModel,
        related_name='orders',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'
