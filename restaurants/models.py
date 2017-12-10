from django.db import models

import datetime



class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50, default="Kathmandu", blank=False)
    location = models.CharField(max_length=50, blank=True)
    open_time = models.TimeField(default=datetime.time(9, 00))
    close_time = models.TimeField(default=datetime.time(18, 00))

    def __str__(self):
        return self.name
