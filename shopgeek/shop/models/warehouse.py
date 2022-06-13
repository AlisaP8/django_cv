from django.db import models


class Warehouse(models.Model):
    name = models.CharField(max_length=64, verbose_name='название')
    receipt_date = models.DateTimeField(verbose_name='дата поступления')
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0, verbose_name='цена')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='единица измерения')
    vendor_name = models.CharField(max_length=250, verbose_name='имя поставщика')
