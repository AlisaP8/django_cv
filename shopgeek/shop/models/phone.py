from django.db import models
from shop.models import Warehouse
from django.contrib.sites.models import Site


class Phone(models.Model):
    desc = models.CharField(max_length=250)
    new_model = models.ManyToManyField(Warehouse)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.desc
