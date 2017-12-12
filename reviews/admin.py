from django.contrib import admin

from .models import ReviewRestaurant, ReviewFood

model_classes = [ReviewFood, ReviewRestaurant]

for model_class in model_classes:
    admin.site.register(model_class)
