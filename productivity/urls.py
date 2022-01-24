from django.urls import path
from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path("knowledge", views.meetups, name="knowledge"),
     path("name", views.get_name, name="get_name")
]