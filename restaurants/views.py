from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from .models import Restaurant
from .forms import RestaurantCreateForm

#function based views

def restaurant_create(request):
    form  = RestaurantCreateForm()
    errors = None

    if request.method == "POST":
        form = RestaurantCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/restaurants/")
        if form.errors:
            errors = form.errors

    template_name = 'restaurants/restaurant_create.html'
    context = {"form": form, "errors": errors}
    return render(request, template_name, context)



def restaurant_list(request):
    template_name = 'restaurants/restaurant_list.html'
    queryset = Restaurant.objects.all()
    context = {
        "restaurants": queryset,
    }
    return render(request, template_name, context)

def restaurant_detail(request, slug):
    template_name = 'restaurants/restaurant_detail.html'
    queryset = Restaurant.objects.filter(slug__iexact = slug).first()
    context = {
        "restaurant": queryset,
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

