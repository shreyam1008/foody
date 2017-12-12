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

def food_detail(request):
    template_name = ''
    context = {

    }
    return render(request, template_name, context)
