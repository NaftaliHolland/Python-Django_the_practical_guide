from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "blog/index.html", {"something" : "Something from views", "title" : ""})

def posts(request):
    return render(request, "blog/blog_list.html")

def blog_post(request, slug):
    return render(request, "blog/post.html", {"post" : slug})