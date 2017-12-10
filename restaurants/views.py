from django.shortcuts import render
from django.views.generic import ListView
from .models import Restaurant

#function based views

def restaurant_list(request):
    template_name = 'restaurants/restaurant_list.html'
    queryset = Restaurant.objects.all()
    context = {
        "restaurants": queryset,
    }
    return render(request, template_name, context)














#
# #class based views
# class RestaurantListView(ListView):
#     template_name = "restaurants/listy.html"
#
#     def get_context_data(self, **kwargs):
#         context = super(RestaurantListView, self).get_context_data(**kwargs)
#         context['test'] = 'the test data    '
#         return context

