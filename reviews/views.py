from django.shortcuts import render

def review_list(request):
    template_name = "reviews/review_list.html"

    context = {
        'test': "hello world"
    }
    return render(request, template_name, context)

def review_create(request):
    template_name = "reviews/review_create.html"

    context = {
        'test': "hello world create"
    }
    return render(request, template_name, context)


