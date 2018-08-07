from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError



def validate_nyn(value):
    choices = ['no', 'yes', 'ne'
                'NO', 'YES', 'NE']
    if value not in choices:
        raise ValidationError(" not in choice 'yes, no or ne' ")


class Restaurant(models.Model):
    # owner =         models.ForeignKey(User, on_delete=models.CASCADE)
    id  =           models.CharField(primary_key=True, max_length=150)
    name =          models.CharField(max_length=150)
    bike_parking = models.CharField(max_length=10, default="NE", validators=[validate_nyn])
    car_parking = models.CharField(max_length=10, default="NE", validators=[validate_nyn])
    smoking = models.CharField(max_length=10, default="NE", validators=[validate_nyn])
    vat = models.CharField(max_length=10, default="NE", validators=[validate_nyn]) #no yes ne
    prange = models.CharField(max_length=10, default="NE", validators=[validate_nyn]) # no yes ne
    delivery = models.CharField(max_length=10, default="NE", validators=[validate_nyn])

    def __str__(self):
        return self.name


class Food(models.Model):

    restaurant =    models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="res")
    name =          models.CharField(max_length=30, unique=True)
    price =         models.PositiveSmallIntegerField(blank=False)
    votes =         models.IntegerField(blank=False, default=0)

    def __str__(self):
        return self.name


class User(models.Model):

    email = models.EmailField(primary_key=True, blank=False, validators=[validate_email])
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Preference(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='use')
    bike_parking = models.CharField(max_length=50, default="NE", validators=[validate_nyn])
    car_parking = models.CharField(max_length=50, default="NE", validators=[validate_nyn])
    smoking = models.CharField(max_length=50, default="NE", validators=[validate_nyn])
    vat = models.CharField(max_length=50, default="NE", validators=[validate_nyn])
    prange = models.CharField(max_length=50, default="NE", validators=[validate_nyn])
    delivery = models.CharField(max_length=50, default="NE", validators=[validate_nyn])

    def __str__(self):
        return ("Pref of " + str(self.user))
    




