from django.db import models
from shop.models import Warehouse


class Phone(models.Model):
    descriptions = models.CharField(max_length=250)
    model = models.ForeignKey(Warehouse, on_delete=models.CASCADE)

    def __str__(self):
        return self.descriptions
