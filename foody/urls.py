from django.contrib import admin
#django 2.0 way of url
from django.urls import path
#django 1.11 way of url
from django.urls import re_path

#to access templates without views
from django.views.generic.base import TemplateView

#access templates with help of views
from restaurants.views import restaurant_list, restaurant_detail, restaurant_create


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
    path('restaurants/', restaurant_list, name='restaurants'),
    path('restaurants/create', restaurant_create, name='create'),
    path('restaurants/<slug>', restaurant_detail, name='detail'),

    path('reviews/', TemplateView.as_view(template_name="temp.html"), name='reviews'),
    path('foods/', TemplateView.as_view(template_name="temp.html"), name='foods'),
    path('profile/', TemplateView.as_view(template_name="temp.html"), name='profile'),
    path('logout/', TemplateView.as_view(template_name="temp.html"), name='logout'),
    path('login/', TemplateView.as_view(template_name="temp.html"), name='login'),
]

# #old way 1.11
# urlpatterns = [
#     re_path(r'^admin/$', admin.site.urls),
# ]
