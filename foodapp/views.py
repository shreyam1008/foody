from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import User, Food, Restaurant

@csrf_exempt
def user_reg(request):

    if request.method =="GET":
        return JsonResponse({"hello there": "general kenobi"})
    elif request.method == 'POST':
        data = request.POST
        print(data)
        User.objects.create(email=data['email'], name=data['name'])


    return HttpResponseRedirect("")


def restaurant_fill(res_list):
    for res in res_list:
        if not Restaurant.objects.filter(res.get('id')):
            Restaurant.objects.create(id=res.get('id'), name=res.get('name'))


@csrf_exempt
def food_add(request):

    if request.method =="GET":
        return JsonResponse({"hello there": "general kenobi"})
    elif request.method == 'POST':
        data = request.POST
        print(data)
        #after restauratn
        Food.objects.create(name=data['name'], price=data['price'])


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
                         }
    )





