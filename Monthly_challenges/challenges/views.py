from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

monthly_challenges = {
    "January" : "Make android apps",
    "February" : "Start going to the gym twice a week",
    "March" : "Eat meat",
    "April" : "Read alot",
    "May" : "Get a new laptop",
    "June" : "Read more",
    "July" : "Eat more meat",
    "August" : "Definatelly not eat vegetables",
    "September" : "What should I do ? Eat more meat",
    "October" : "O don't know man",
    "November" : "What to do",
    "December" : "Make a plan for the next year"
}

myresponse = ""
def monthly_challenge_by_number(request, month):
    try:
        myresponse = monthly_challenges[month]
        return HttpResponse(myresponse)
    except:
        return HttpResponseNotFound("We don't have that sorry")

'''def monthly_challenge(request, month):
    myresponse = ""
    if month == "January":
        myresponse += "It's january"

    elif month == "February":
        myresponse += "It's february baiby"

    else:
        return HttpResponseNotFound("Page Not found")

    return HttpResponse(myresponse)'''