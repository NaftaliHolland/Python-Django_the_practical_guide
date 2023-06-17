from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

def monthly_challenge(request, month):
    myresponse = ""
    if month == "January":
        myresponse += "It's january"

    elif month == "February":
        myresponse += "It's february baiby"

    else:
        return HttpResponseNotFound("Page Not found")

    return HttpResponse(myresponse)