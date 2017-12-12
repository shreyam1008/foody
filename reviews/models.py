from django.db import models

from restaurants.models import Restaurant
from foods.models import Food

RATING_CHOICES = (
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)

class ReviewRestaurant(models.Model):

    restaurant      = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restau')

    rating          = models.SmallIntegerField(default=0, choices=RATING_CHOICES)
    comment_head    = models.CharField(max_length=50, null=True, blank=True)
    comment_body    = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.comment_head

class ReviewFood(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='rest')
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='foo')

    rating = models.SmallIntegerField(default=0, choices=RATING_CHOICES)
    comment_head = models.CharField(max_length=50, null=True, blank=True)
    comment_body = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.comment_head


