from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
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
    "December" : None
}

def index(request):
    month_list = list(monthly_challenges.keys())

    response = render(request, "challenges/index.html", {"months" : month_list})
    return HttpResponse(response)
    
myresponse = ""
#This function will redirect to a month depending on the number passed 1 - 12 inclusive
def monthly_challenge_by_number(request, month):
    #create a list of keys from the dictionary monthly_challenges
    challenges = list(monthly_challenges.keys())
    #We index into the keys using the month passed in as a parameter
    #return HttpResponseRedirect("challenges/" + challenges[month - 1]) Hard coded path there has to be a better way
    if month > len(challenges):
        return HttpResponseNotFound("Not here")
    challenge = challenges[month]
    redirect_url = reverse("challenges", args=[challenge])
    
    return HttpResponseRedirect(redirect_url)

def monthly_challenge(request, month):
    try:
        myresponse = monthly_challenges[month]
        #page_data = "<h1>{}</h1>".format(myresponse)
        page_data = render(request, "challenges/challenge.html", {"challenge" : myresponse, "challenge_month" : month.lower()})
        return HttpResponse(page_data)
    except:
        return HttpResponseNotFound("We don't have that sorry")