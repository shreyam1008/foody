from django.db import models
from django.db.models.signals import pre_save
import datetime


from .utils import unique_slug_generator




class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50, default="Kathmandu", blank=False)
    location = models.CharField(max_length=50, blank=True)
    open_time = models.TimeField(default=datetime.time(9, 00))
    close_time = models.TimeField(default=datetime.time(18, 00))
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    slug = models.SlugField(null=True, blank=True)


    def __str__(self):
        return self.name


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=Restaurant)
