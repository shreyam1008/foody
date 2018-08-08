from django.contrib import admin
#django 2.0 way of url
from django.urls import path, include
#django 1.11 way of url
from django.urls import re_path

#to access templates without views
from django.views.generic.base import TemplateView

#access templates with help of views
from restaurants.views import restaurant_list, restaurant_detail, restaurant_create
from foods.views import food_list, food_detail, food_create
from reviews.views import review_list, review_create
from apis.views import places_list, place_detail

from foodapp.views import user_reg, food_add, res_recomm, pref_add, pref_get, res_edit, food_vote

from chatbot import urls as chatbot_urls

from testview import test_func

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="home.html"), name="home"),

    path('restaurants/', restaurant_list, name='restaurants'),
    path('restaurants/create/', restaurant_create, name='create'),
    path('restaurants/<slug>/', restaurant_detail, name='detail'),

    path('foods/', food_list, name='foods'),
    path('foods/create/', food_create, name='foocreate'),
    path('foods/<int:res_id>/<food_name>/', food_detail, name='foodetail'),

    path('reviews/', review_list, name='reviews'),


    path('profile/', TemplateView.as_view(template_name="temp.html"), name='profile'),
    path('logout/', TemplateView.as_view(template_name="temp.html"), name='logout'),
    path('login/', TemplateView.as_view(template_name="temp.html"), name='login'),

    # path('apis/places/'),
    path('api/places/lat=<lat>&long=<long>/', places_list, name='placelist'),
    path('api/pdetail/id=<id>/', place_detail, name='placedetail'),
    #chatbot api
    # path('api/chatbot/', )

    #post apis
    path('api/newuser/', user_reg, name='user_reg'),

    path('api/newfood/', food_add, name='food_add'),
    path('api/userprefrence/', pref_add, name='user_pref'),

    #post for restaurant edit. or add prefrences
    path('api/editres/', res_edit, name='res_edit'),


    path('api/reccomres/user=<email>/', res_recomm, name='res_recomm'),


    path('api/userprefrence/user=<email>/', pref_get, name='user_pref'),

    #when user thums up or down. PUT
    path('api/voting/', food_vote, name="food_vote")



    path('chatbot/', include(chatbot_urls)),

    #test
    path('test/', test_func)
]

# #old way 1.11
# urlpatterns = [
#     re_path(r'^admin/$', admin.site.urls),
# ]
