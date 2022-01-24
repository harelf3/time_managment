from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    template = 'productivity/index2.html'
    return render(request,template)

def meetups(request):
    template = 'productivity/knowledge.html'
    return render(request,template)

