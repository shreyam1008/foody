from django.db import models

from restaurants.models import Restaurant

class Food(models.Model):

    restaurant =    models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name =          models.CharField(max_length=30, unique=True)
    price =         models.PositiveSmallIntegerField()

    timestamp =     models.DateTimeField(auto_now_add=True)
    updated =       models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



