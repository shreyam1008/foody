from django.db import models



class Restaurant(models.Model):
    # owner =         models.ForeignKey(User, on_delete=models.CASCADE)
    id  =           models.CharField()
    name =          models.CharField()
    bike_parking = models.BooleanField()
    car_parking = models.BooleanField()
    smoking = models.BooleanField()
    # vat = models.CharField(max_length=50, default="NE", validators=[validate_vat]) #no yes ne
    # prange = models.CharField(max_length=50, default="NE", validators=[validate_prange]) # no yes ne
    delivery = models.BooleanField()

    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name


class Food(models.Model):

    restaurant =    models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="res")
    name =          models.CharField(max_length=30, unique=True)
    price =         models.PositiveSmallIntegerField(blank=False)
    votes =         models.IntegerField()

    def __str__(self):
        return self.name


class User(models.Model):

    name = models.CharField(max_length=60, blank=False)
    email = models.EmailField(blank=False)
