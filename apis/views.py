from django.shortcuts import render
from django.http import JsonResponse

import requests

def places_list(request):
    response = {"aa": "aa",
                    "cc": "dd"}

    return JsonResponse(response)