from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def user_reg(request):

    if request.method =="GET":
        return JsonResponse({"hello there": "general kenobi"})
    elif request.method == 'POST':
        a = request.POST
        print(a)

    return HttpResponseRedirect("")



@csrf_exempt
def food_add(request):

    if request.method =="GET":
        return JsonResponse({"hello there": "general kenobi"})
    elif request.method == 'POST':
        a = request.POST
        print(a)

    return HttpResponseRedirect("")


@csrf_exempt
def user_pref(request):

    if request.method =="GET":
        return JsonResponse({"hello there": "general kenobi"})
    elif request.method == 'POST':
        a = request.POST
        print(a)

    return HttpResponseRedirect("")


@csrf_exempt
def res_recomm(request):

    if request.method =="GET":
        return JsonResponse({"hello there": "general kenobi"})
    elif request.method == 'POST':
        a = request.POST
        print(a)

    return HttpResponseRedirect("")