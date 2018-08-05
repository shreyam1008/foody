from django.contrib import admin

from .models import Food, Restaurant, User
admin.site.register(Food)
admin.site.register(Restaurant)
admin.site.register(User)

