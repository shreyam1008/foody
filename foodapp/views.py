from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import User, Food, Restaurant, Preference

@csrf_exempt
def user_reg(request):

    if request.method =="GET":
        return JsonResponse({"hello there": "general kenobi"})
    elif request.method == 'POST':
        data = request.POST
        print(data)
        userinstance = User.objects.create(email=data['email'], name=data['name'])
        userinstance.save()
        prefinstance = Preference.objects.create(user_id = data['email'])
        prefinstance.save()


    return HttpResponseRedirect("")


def restaurant_fill(res_list):
    for res in res_list:
        if not Restaurant.objects.filter(id = res.get('id')):
            instance = Restaurant.objects.create(id=res.get('id'), name=res.get('name'))
            instance.save()

#pPUT for food/menu
@csrf_exempt
def food_add(request):

    if request.method =="GET":
        return JsonResponse({"hello there": "general kenobi"})
    elif request.method == 'POST':
        data = request.POST
        print(data)
        instance = Food.objects.create(restaurant_id=data['placeid'],
                                       name=data['name'],
                                       price=data['price'])
        instance.save()
        print("ok done")

    return HttpResponseRedirect("")


#countig votes
@csrf_exempt
def food_vote(request):

    if request.method =="GET":
        return JsonResponse({"hello there ": "general kenobi"})
    elif request.method == 'POST':
        data = request.POST
        print(data)

        instance = Food.objects.filter(restaurant=data['placeid']).get(name=data['name'])

        if data['vote'] == "UP":
            instance.votes += 1

        if data['vote'] == "DOWN":
            instance.votes -= 1


    return HttpResponseRedirect("")


@csrf_exempt
def pref_add(request):

    if request.method =="GET":
        return JsonResponse({"hello there ": "general kenobi"})
    elif request.method == 'POST':
        data = request.POST
        print(data)

        x = Preference.objects.filter(user__email=data['email'])

        if not x:
            instance = Preference.objects.create(   user = data['email'],
                                                    bike_parking=data['bike_parking'],
                                                    car_parking=data['car_parking'],
                                                    smoking=data['smoking'],
                                                    vat=data['vat'],
                                                    prange=data['prange'],
                                                    delivery=data['delivery'],
                                                 )
            instance.save()

    return HttpResponseRedirect("")

def pref_get(request, email):

    # get from database.create
    x = Preference.objects.get(user__email=email)


    response = {}
    if x:
        response = {
                "email": email,
                "bike_parking" : x.bike_parking,
                "car_parking" : x.car_parking,
                "smoking" : x.smoking,
                "vat" : x.vat,
                "prange" : x.prange,
                "delivery" : x.delivery
            }

    return JsonResponse(response)


@csrf_exempt
def res_edit(request):

    if request.method =="GET":
        return JsonResponse({"hello there ": "general kenobi"})
    elif request.method == 'POST':
        data = request.POST
        print(data)

        instance = Restaurant.objects.get(id=data.resid)
        instance.bike_parking = data['bike_parking']
        instance.car_parking =  data['car_parking']
        instance.delivery = data['delivery']
        instance.smoking = data['smoking']
        instance.prange = data['prange']
        instance.vat = data['vat']

        instance.save()

    return HttpResponseRedirect("")


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
