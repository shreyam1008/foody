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
        response_items = {"id": data['id'],
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