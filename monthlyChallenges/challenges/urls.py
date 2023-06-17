from django.urls import path
from . import views
#list of urls to be supported and the function that should be trigered when the path is reached
urlpatterns = [
    path("january", views.index),
    path("february", views.feb)
]