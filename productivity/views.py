from django.shortcuts import render
from django.http import HttpResponse
from math import floor
# Create your views here.

def index(request):
    template = 'productivity/index2.html'
    return render(request,template)



from django.http import HttpResponseRedirect

from productivity.models import Data,Connections
from .form import DataForm, ConnectionForm

def knowledge(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DataForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            subjects = form.cleaned_data['subjects']
            entry_type = form.cleaned_data['entry_type']
            url = form.cleaned_data['url']
            desc = form.cleaned_data['desc']
            listing = Data.objects.create(Subjects=subjects,Entry_type=entry_type,url=url,desc=desc)
            listing.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form = DataForm()
            return render(request, 'productivity/knowledge.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DataForm()

    return render(request, 'productivity/knowledge.html', {'form': form})


def network(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ConnectionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            contact =form.cleaned_data['contact']
            title = form.cleaned_data['title']
            desc = form.cleaned_data['desc']
            field = form.cleaned_data['field']
            person = Connections.objects.create(full_name=full_name,contact=contact,title=title,desc=desc,field=field)
            person.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form = ConnectionForm()
            template = 'productivity/network.html'
        # phrase see how many connections have and /10 and then i got level and curnet 
            all_entries = Connections.objects.all()
            lenpeople = len(all_entries)
            level = floor(lenpeople/10)
        return render(request, template, {'form': form,'people':lenpeople,'level':level})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ConnectionForm()
        template = 'productivity/network.html'
        # phrase see how many connections have and /10 and then i got level and curnet 
        level = "25"
        all_entries = Connections.objects.all()
        lenpeople = len(all_entries)
        level = floor(lenpeople/10)
    return render(request, template, {'form': form,'people':lenpeople,'level':level})


def networkdb(request):
    form = ConnectionForm()
    all_entries = Connections.objects.all()
    lenpeople = len(all_entries)
    level = floor(lenpeople/10)
    all_entries = Connections.objects.all()
    template = 'productivity/networkdb.html'
    return render(request, template,{"entries":all_entries,'form': form,'people':lenpeople,'level':level})
