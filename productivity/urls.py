from django.urls import path
from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path("knowledge", views.knowledge, name="knowledge"),
     path("network", views.network, name="network"),
     path("network/network", views.networkdb, name="networkdb"),
     path("network/<str:subj>", views.networkevents, name="networkevents"),
]