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
def pref_add(request):

    if request.method =="GET":
        return JsonResponse({"hello there ": "general kenobi"})
    elif request.method == 'POST':
        a = request.POST
        print(a)

    return HttpResponseRedirect("")

@csrf_exempt
def res_edit(request):

    if request.method =="GET":
        return JsonResponse({"hello there ": "general kenobi"})
    elif request.method == 'POST':
        a = request.POST
        print(a)

    return HttpResponseRedirect("")

def pref_get(request, email):
    return JsonResponse({"email": email,
                            "bike_parking": "YES",
                                "car_parking": "YES",
                                    "smoking": "ANY",
                                        "vat": "ANY",
                                            "prange": "ANY",
                                                "delivery": "NO"
                         }
                        )

def res_recomm(request, email):
    return JsonResponse({"results": [
                                        "ChIJNWXIzkUZ6zkR272DWRQBzOs",
                                        "ChIJNWXIzkUZ6zkR272DWRQBzOs",
                                        "ChIJNWXIzkUZ6zkR272DWRQBzOs",
                                        "ChIJNWXIzkUZ6zkR272DWRQBzOs",
                                        "ChIJ3cbjcWYZ6zkROlDr-i5TJaI",
                                        "ChIJj9w2oDcZ6zkR2-Iwm9Q4nZk",
                                        ]
                         })





