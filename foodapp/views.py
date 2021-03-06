from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import User, Food, Restaurant, Preference
    # , RateReview

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


def user_name(request, email):
    name = User.objects.get(email=email).name

    return JsonResponse(
        {"email": email, "name": name}
    )



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
            instance.save()

        if data['vote'] == "DOWN":
            instance.votes -= 1
            instance.save()


    return HttpResponseRedirect("")


@csrf_exempt
def pref_add(request):

    if request.method =="GET":
        return JsonResponse({"hello there ": "general kenobi"})
    elif request.method == 'POST':
        data = request.POST
        print(data)

        x = Preference.objects.get(user__email=data['email'])

        #add update
        if x:
            x.bike_parking = data['bike_parking']
            x.car_parking = data['car_parking']
            x.smoking = data['smoking']
            x.vat = data['vat']
            x.prange = data['prange']
            x.delivery = data['delivery']
            x.save()

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

        instance = Restaurant.objects.get(id=data['placeid'])
        instance.bike_parking = data['bike_parking']
        instance.car_parking =  data['car_parking']
        instance.delivery = data['delivery']
        instance.smoking = data['smoking']
        instance.prange = data['prange']
        instance.vat = data['vat']

        instance.save()

    return HttpResponseRedirect("")



def res_info(request, rest_id):


    x = Restaurant.objects.get(id=rest_id)
    # x = Restaurant.objects.get()

    response = {}
    if x:
        response = {
            "bike_parking": x.bike_parking,
            "car_parking": x.car_parking,
            "smoking": x.smoking,
            "vat": x.vat,
            "prange": x.prange,
            "delivery": x.delivery
        }

    return JsonResponse(response)

def res_recomm(request, email):


    return JsonResponse({"results": [
                                        "ChIJywHkp8kZ6zkRliM0q7MuHcI",
                                        "ChIJHUvbqzQY6zkRrqQtyHiVDIg",
                                        "ChIJNWXIzkUZ6zkR272DWRQBzOs",
                                        "ChIJ1TqSqcsZ6zkRfDNVCDsswxA",
                                        "ChIJ3cbjcWYZ6zkROlDr-i5TJaI",
                                        "ChIJj9w2oDcZ6zkR2-Iwm9Q4nZk",
                                        ]
                         }
    )

# @csrf_exempt
# def chat(request):
#     #for random resposne
#     import random
#     import time
#
#     if request.method =="GET":
#         return JsonResponse({"hello there ": "general kenobi"})
#     elif request.method == 'POST':
#         data = request.POST
#         print(data)
#
#         time_now = str(int(round(time.time() * 1000)))
#         greet_list = ["hi", "hello", "hey"]
#         greet_response = [
#                             "Hey Food enthusist. Thanks for chooing BHoodie",
#                             "I am BHAUJU. Your food ordering chatbot.",
#                             "How can i be of your assistance senpei?"
#                           ]
#
#         if data['message'].lower() in greet_list:
#
#             bot_resp = random.choice(greet_response)
#
#         else:
#             bot_resp = "Sorry i am not smart enough to understand you yet ONNI CHAN"
#
#         #
#         # {'time': ['09:30 PM'], 'receiver': ['ChIJofNoSV0Z6zkRRjem9lYXvQ4'], 'message': ['hi'],
#         #  'sender': ['bcbcbc@gmail.com']}
#         #  resp =
#
#         response = {
#             "time": time_now,
#             "receiver": data['sender'],
#             "message": bot_resp,
#             "sender": Restaurant.objects.get(id = data['receiver']).name
#
#         }
#         return JsonResponse(response)
#
#
#     return HttpResponseRedirect("")
#

#from chatterbot
@csrf_exempt
def chat(request):

    import time

    from chatterbot import ChatBot
    from chatterbot.trainers import ListTrainer
    from chatterbot.trainers import ChatterBotCorpusTrainer

    bot = ChatBot("test")
    conversation = [
        "hello",
        "Thanks for chooing Bhoodie.",
        "You are great.",
        "Thank you very much",
        "What is your name?",
        "I am BHAUJU. Your food ordering chatbot.",
        "Tell me something in japanese",
        "Hello Onni Chan. I am here to serve you"
    ]
    # bot.set_trainer(ListTrainer)
    # bot.train(conversation)#train from above list
    # bot.set_trainer(ChatterBotCorpusTrainer)
    # bot.train('chatterbot.corpus.english.greetings')
    # bot.train('chatterbot.corpus.english.food')
    # bot.train('chatterbot.coprus.english.humor')


    if request.method =="GET":
        return JsonResponse({"hello there ": "general kenobi"})
    elif request.method == 'POST':
        data = request.POST
        print(data)

        location = data['userloc'].split(',')
        print(location)
        data_type = data['type']
        #
        # #if general msg GM
        # if data_type == "GM":
        #     # check if GM matches any specific msg you want for specific actions
        #     if data['message'].lower() == "restaurant name?":
        #     # pdetails bring naem
        #     if data['message'].lower() == "restaurant location?":
        #     # pdetails bring address, http://maps.google.com/maps?daddr=27.689092,85.327423 bring location
        #     if data['message'].lower() == "restaurant time?":
        #     # pdetails bring opening hours
        #     if data['message'].lower() == "is is open?":
        #     # yes
        #     # same for no, webisite, menus
        #
        #     # delivery
        #     if data['message'].lower() == "order food?":
        #     # pdetails show complete menu
        #
        # if data_type == "OM":
        #     pass
        #
        # ####making trigger word condition
        #



        bot_resp = bot.get_response(data['message'])
        msg_type = "GM"

        time_now = str(int(round(time.time() * 1000)))
        response = {
            "time": time_now,
            "receiver": data['sender'],
            "message": str(bot_resp),
            "sender": Restaurant.objects.get(id = data['receiver']).name
            "type": msg_type

        }
        return JsonResponse(response)


    return HttpResponseRedirect("")




#
# @csrf_exempt
# def review_add(request):
#
#     if request.method =="GET":
#         return JsonResponse({"hello there": "general kenobi"})
#     elif request.method == 'POST':
#         data = request.POST
#         print(data)
#
#         instance = RateReview.objects.create(restaurant__id=data['placeid'],
#                                              email=data['email'],
#                                              rating=data['rating'],
#                                              comment=data['comment'],
#                                              )
#         instance.save()
#
#         print("ok done")
#
#     return HttpResponseRedirect("")
#
#
# def review_get(request, rest_id):
#
#     # get from database.create
#     data = RateReview.objects.filter(restaurant__id=rest_id)
#
#
#     instance = []
#     for x in data:
#         if x:
#             instance.append(
#                 {
#                     "email": x.email,
#                     "rating": x.rating,
#                     "comment" : x.comment
#                 }
#             )
#
#     response = {"reviews": instance}
#
#     return JsonResponse(response)