from django.db import models
from django.dispatch import Signal, receiver

some_signal = Signal()


class HitCount(models.Model):
    path = models.CharField(max_length=512, primary_key=True)
    hits = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.path} ({self.hits})'

    def save(self, *args, **kwargs):
        some_signal.send(self, test=1)
        return super().save(*args, **kwargs)


@receiver(some_signal)
def post_save_hit(sender, *args, **kwargs):
    print(sender)
