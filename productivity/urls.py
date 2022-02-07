from django.urls import path
from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path("knowledge", views.knowledge, name="knowledge"),
     path("network", views.network, name="network"),
     path("network/network", views.networkdb, name="networkdb"),
     path("network/<str:subj>", views.networkevents, name="networkevents"),
     path("knowledge/<str:subj>/<str:type>", views.knowledgeresources, name="knowledgeresources"),
     path('player',views.player,name="player"),
     path('emailsender',views.emailsender,name="emailsender"),
]