from django.shortcuts import render


from .models import Food

def food_list(request):
    template_name = 'foods/food_list.html'
    query_set = Food.objects.all()
    context = {
        'foods': query_set
    }
    return render(request, template_name, context)

def food_detail(request):
    template_name = ''
    context = {

    }
    return render(request, template_name, context)

def food_create(request):
    template_name = 'foods/food_create.html'
    context = {

    }
    return render(request, template_name, context)