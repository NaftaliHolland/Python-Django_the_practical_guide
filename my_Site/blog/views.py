from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def index(request):
    latest_posts = Post.objects.order_by("-date")[:3]
    context = {"posts" : latest_posts}
    return render(request, "blog/index.html", context)

def posts(request):
    return render(request, "blog/all_posts.html")

def blog_post(request, slug):
    return render(request, "blog/post-detail.html", {"post" : slug})