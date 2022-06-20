from django.db import models
from shop.models import Warehouse


class Headphones(models.Model):
    desc = models.CharField(max_length=250)
    new_model = models.ManyToManyField(Warehouse)

    def __str__(self):
        return self.desc
