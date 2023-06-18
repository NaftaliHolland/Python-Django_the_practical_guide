from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

myresponse = ""
def monthly_challenge_by_number(request, month):
    if month == 1:
        myresponse = "wazaa"
    elif month == 2:
        myresponse = "Feb baiby"
    else:
        return HttpResponseNotFound("We don't have that sorry")
    return HttpResponse(myresponse)

def monthly_challenge(request, month):
    myresponse = ""
    if month == "January":
        myresponse += "It's january"

    elif month == "February":
        myresponse += "It's february baiby"

    else:
        return HttpResponseNotFound("Page Not found")

    return HttpResponse(myresponse)