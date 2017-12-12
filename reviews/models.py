from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from restaurants.models import Restaurant
from foods.models import Food

class Review(models.Model):

    restaurant      = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='rest')
    food            = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='foo')

    rating          = models.SmallIntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    comment_head    = models.CharField(max_length=50, null=True, blank=True)
    comment_body    = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.comment_head


