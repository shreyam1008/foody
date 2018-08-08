from django.shortcuts import render
from django.http import JsonResponse
from foodapp.views import restaurant_fill
from foodapp.models import Food
import requests, json


def places_list(request, lat, long):
    key = "AIzaSyA6pnyEvSVg7yOeCbtjaJi5pQHgA668aYw"
    location = "{lat},{long}".format(lat=lat, long=long)
    # radius = "2500"
    # link = f"https://maps.googleapis.com/maps/api/place/nearbysearch/output?{parameters}"
    link = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius=2500&type=restaurant&key={key}".format(
        location=location, key=key)
    json_data = requests.get(link).json()
    # print(json_data)
    res_list = []

    open_default = {
        "open_now": None
    }
    for data in json_data['results']:
        response_items = {"id": data.get('place_id'),
                          "name": data.get('name'),
                          "location": {"lat": data['geometry']['location']['lat'],
                                       "lng": data['geometry']['location']['lng']},
                          "open": data.get("opening_hours", open_default).get("open_now"),
                          "rating": data.get("rating"),
                          }

        res_list.append(response_items)

        # if (len(res_list) == 20):
        #     token = json_data.get('next_page_token')
        #     link += "&pagetoken={token}".format(token=token)
        # elif (len(res_list) >= 30):
        #     break
        # else:
        #     pass

    # to fill res in database
    restaurant_fill(res_list)

    response = {"results": res_list}
    return JsonResponse(response)


def get_photos(photos):
    photo_list = []

    if photos != None:
        for photo in photos:
            data = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=600&photoreference={ref}&key=AIzaSyA6pnyEvSVg7yOeCbtjaJi5pQHgA668aYw".format(
                ref=str(photo['photo_reference']))
            photo_list.append(data)
    return (photo_list)


def get_reviews(reviews):
    # add reviews from other sides
    review_list = []
    if reviews != None:
        for review in reviews:
            data = {
                "name": review.get('author_name'),
                "text": review.get('text')
            }
            review_list.append(data)
    return (review_list)


# get request of foods/meny
def get_menu(res_id):
    # get from database.create
    data = Food.objects.filter(restaurant=res_id)

    response = []

    if data:
        for x in data:
            response.append(
                {"name": x.name, "price": x.price, "votes": 3}
            )
    return (response)


def place_detail(request, id):
    key = "AIzaSyA6pnyEvSVg7yOeCbtjaJi5pQHgA668aYw"
    link = "https://maps.googleapis.com/maps/api/place/details/json?placeid={id}&key={key}".format(id=id, key=key)
    response = requests.get(link)
    json_data = response.json()['result']

    opening_default = {
        "weekday_text": [
            "N/A",
        ]
    }

    response_items = {"name": json_data.get('name'),
                      "id": id,
                      "address": json_data.get('formatted_address'),
                      "formatted_phone_number": json_data.get('formatted_phone_number'),
                      "opening_hours": json_data.get('opening_hours', opening_default).get('weekday_text'),
                      "photos": get_photos(json_data.get('photos')),
                      "review": get_reviews(json_data.get('reviews')),
                      "website": json_data.get('website'),
                      "menu": get_menu(id),

                      "location": {"lat": json_data['geometry']['location']['lat'],
                                   "lng": json_data['geometry']['location']['lng']
                                   }

                      }

    return JsonResponse(response_items)
