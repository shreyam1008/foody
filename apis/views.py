from django.shortcuts import render
from django.http import JsonResponse

import requests, json

def places_list(request, lat, long):

    key = "AIzaSyCLUN6zu45xEvZa9M2RtGGERC7xuj2ZOHg"
    location = "{lat},{long}".format(lat=lat, long=long)
    # radius = "2500"
    # link = f"https://maps.googleapis.com/maps/api/place/nearbysearch/output?{parameters}"
    link = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius=2500&type=restaurant&key={key}".format(location=location, key=key)
    json_data = requests.get(link).json()
    res_list = []
    for data in json_data['results']:
        response_items = {"id": data['place_id'],
                          "name": data['name'],
                          "location": {"lat": data['geometry']['location']['lat'],
                                       "lng": data['geometry']['location']['lng']},
                          "open": True,#laterstr(data['opening_hours']['open_now']),
                          "rating": 123,  # correctino rating extraction later data['raitng']
                          }

        res_list.append(response_items)

        if (len(res_list) == 20):
            token = json_data['next_page_token']
            link += "&pagetoken={token}".format(token=token)
        elif (len(res_list) >= 30):
            break
        else:
            pass

    response = {"results": res_list}
    return JsonResponse(response)

def get_photos(photos):
    photo_list = []
    for photo in photos:
        data = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=600&photoreference={ref}&key=AIzaSyCLUN6zu45xEvZa9M2RtGGERC7xuj2ZOHg".format(ref=str(photo['photo_reference']))
        photo_list.append(data)

    return(photo_list)


def get_reviews(reviews):
    #add reviews from other sides
    review_list = []
    for review in reviews:
        data = {
            review['author_name']: review['text']
        }
        review_list.append(data)
    return (review_list)


def place_detail(request, id):
    key = "AIzaSyCLUN6zu45xEvZa9M2RtGGERC7xuj2ZOHg"
    link = "https://maps.googleapis.com/maps/api/place/details/json?placeid={id}&key={key}".format(id=id, key=key)
    response = requests.get(link)
    json_data = response.json()['result']

    response_items = {"name":json_data['name'],
                        "address":json_data['formatted_address'],
                            "formatted_phone_number":json_data['formatted_phone_number'],
                                "opening_hours":json_data['opening_hours']['weekday_text'],
                                    "photos": get_photos(json_data['photos']),
                                        "review": get_reviews(json_data['reviews']),
                                            "website": json_data['website']
                    }

    return JsonResponse(response_items)





