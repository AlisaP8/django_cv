from django.db import models
from django.db.models import Manager

from shop.models import Warehouse


class DeletedQuerySet(models.QuerySet):
    def not_deleted(self):
        return self.filter(deleted=False)


class DeletedManager(Manager):
    def get_queryset(self):
        # return super().get_queryset().filter(deleted=False)
        return DeletedQuerySet(self.model, using=self._db)

    def not_deleted(self):
        return self.get_queryset().not_deleted()


class Headphones(models.Model):
    descriptions = models.CharField(max_length=250)
    model = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.descriptions
