from django.db import models
from django.core.validators import validate_email


YN_CHOICES = (
    (0, "NO"),
    (1, "YES"),
)

VAT_CHOICES = (
    (0, "NO"),
    (1, "ANY"),
)

RANGE_CHOICES = (
    (0, "ANY"),
    (1, "LOW"),
    (2, "MID"),
    (3, "HIGH"),
)

RATING_CHOICES = (
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)
class Restaurant(models.Model):
    # owner =         models.ForeignKey(User, on_delete=models.CASCADE)
    id  =           models.CharField(primary_key=True, max_length=150)
    name =          models.CharField(max_length=150)
    bike_parking = models.CharField(max_length=10, blank=True, choices=YN_CHOICES)
    car_parking = models.CharField(max_length=10, blank=True, choices=YN_CHOICES)
    smoking = models.CharField(max_length=10, blank=True, choices=YN_CHOICES)
    vat = models.CharField(max_length=10, blank=True, choices=VAT_CHOICES)
    prange = models.CharField(max_length=10, blank=True, choices=RANGE_CHOICES)
    delivery = models.CharField(max_length=10, blank=True, choices=YN_CHOICES)

    def __str__(self):
        return self.name


class Food(models.Model):

    restaurant =    models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="res")
    name =          models.CharField(max_length=30)
    price =         models.PositiveSmallIntegerField(blank=False)
    votes =         models.IntegerField(blank=False, default=0)

    def __str__(self):
        return self.name

class RateReview(models.Model):

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="restua")
    email = models.EmailField(blank=True)
    rating = models.SmallIntegerField(blank=True, choices=RATING_CHOICES)
    comment    = models.CharField(max_length=100, null=True, blank=True)



class User(models.Model):

    email = models.EmailField(primary_key=True, blank=False, validators=[validate_email])
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Preference(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='use')
    bike_parking = models.CharField(max_length=50, default="YES", choices=YN_CHOICES)
    car_parking = models.CharField(max_length=50, default="NO", choices=YN_CHOICES)
    smoking = models.CharField(max_length=50, default="NO", choices=YN_CHOICES)
    vat = models.CharField(max_length=50, default="ANY", choices=VAT_CHOICES)
    prange = models.CharField(max_length=50, default="ANY",  choices=RANGE_CHOICES)
    delivery = models.CharField(max_length=50, default="NO", choices=YN_CHOICES)

    def __str__(self):
        return ("Pref of " + str(self.user))


    




