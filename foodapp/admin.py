from django.contrib import admin
from .models import Food, Restaurant, User, Preference,\
    # RateReview

admin.site.register(Food)
admin.site.register(Restaurant)
admin.site.register(User)
admin.site.register(Preference)
# admin.site.register(RateReview)
