from django.contrib import admin
#django 2.0 way of url
from django.urls import path
#django 1.11 way of url
from django.urls import re_path

#to acess template with views
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
    path('restaurants/', TemplateView.as_view(template_name="temp.html"), name='restaurants'),
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
