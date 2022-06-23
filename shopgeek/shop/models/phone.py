from django.db import models
from django.db.models import Manager

from shop.models import Warehouse
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager


class Phone(models.Model):
    desc = models.CharField(max_length=250)
    new_model = models.ManyToManyField(Warehouse)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)
    objects = Manager()
    on_site = CurrentSiteManager('site')
    # objects = CurrentSiteManager('site')

    def __str__(self):
        return self.desc
