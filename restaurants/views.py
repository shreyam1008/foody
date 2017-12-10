from django.shortcuts import render
from django.views.generic import ListView

#function based views

def restaurant_list(request):
    template_name = 'restaurants/restaurant_list.html'
    context = {
        "test": 'list of restaurants to come'
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

