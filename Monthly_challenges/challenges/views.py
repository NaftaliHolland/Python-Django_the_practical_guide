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
#This function will redirect to a month depending on the number passed 1 - 12 inclusive
def monthly_challenge_by_number(request, month):
    #create a list of keys from the dictionary monthly_challenges
    challenges = list(monthly_challenges.keys())
    #We index into the keys using the month passed in as a parameter
    try:
        return HttpResponse(monthly_challenges[challenges[month]])
    except:
        return HttpResponseNotFound("Not here my man not here")

    

def monthly_challenge(request, month):
    try:
        myresponse = monthly_challenges[month]
        return HttpResponse(myresponse)
    except:
        return HttpResponseNotFound("We don't have that sorry")