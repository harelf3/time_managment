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

from django.http import HttpResponseRedirect
from django import forms
from productivity.models import Person
class NameForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['name']
            fruit = Person.objects.create(name=name)
            fruit.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'productivity/knowledge.html', {'form': form})