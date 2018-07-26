from django.shortcuts import render
from django.http import JsonResponse

import requests

def places_list(request, lat, long):

    response = {"aa": str(lat)+"test1",
                    "cc": str(long)+"bb"}

    return JsonResponse(response)