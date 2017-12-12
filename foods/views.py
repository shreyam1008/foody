from django.http import HttpResponseRedirect
from django.shortcuts import render


from .models import Food
from .forms import FoodCreateForm

def food_list(request):
    template_name = 'foods/food_list.html'
    query_set = Food.objects.all()
    context = {
        'foods': query_set
    }
    return render(request, template_name, context)

def food_create(request):

    form = FoodCreateForm()
    errors = None

    if request.method == "POST":
        form = FoodCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/foods/")

        if form.errors:
            errors = form.errors
    template_name = 'foods/food_create.html'
    context = {
        "form": form, "errors": errors
    }
    return render(request, template_name, context)

def food_detail(request, res_id, food_name):
    template_name = 'foods/food_detail.html'
    queryset = Food.objects.filter(restaurant = res_id).filter(name__iexact=food_name).first()
    # queryset = Food.objects.filter(name__iexact = food_name)
    context = {
        "food": queryset,
    }
    return render(request, template_name, context)
