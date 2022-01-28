from django.shortcuts import render
from django.http import HttpResponse
from math import floor
# Create your views here.

def index(request):
    template = 'productivity/index2.html'
    return render(request,template)



from django.http import HttpResponseRedirect

from productivity.models import Data,Connections,NetworkEvents
from .form import DataForm, ConnectionForm,EventsForm

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
        if "addconnection" in request.POST:
            connection_form = ConnectionForm(request.POST)
            # check whether it's valid:
            if connection_form.is_valid():
                full_name = connection_form.cleaned_data['full_name']
                contact =connection_form.cleaned_data['contact']
                title = connection_form.cleaned_data['title']
                desc = connection_form.cleaned_data['desc']
                field = connection_form.cleaned_data['field']
                person = Connections.objects.create(full_name=full_name,contact=contact,title=title,desc=desc,field=field)
                person.save()
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                event_form = EventsForm()
                connection_form = ConnectionForm()
                template = 'productivity/network.html'
            # phrase see how many connections have and /10 and then i got level and curnet 
                all_entries = Connections.objects.all()
                lenpeople = len(all_entries)
                level = floor(lenpeople/10)
            return render(request, template, {'connection_form': connection_form,"event_form":event_form,'people':lenpeople,'level':level})
        if "addevent" in request.POST:
            eventsform = EventsForm(request.POST)
            if eventsform.is_valid():
                event_type = eventsform.cleaned_data['event_type']
                website_name =eventsform.cleaned_data['website_name']
                website_url = eventsform.cleaned_data['website_url']
                event = NetworkEvents.objects.create(event_type=event_type,website_name=website_name,website_url=website_url)
                event.save()
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                event_form = EventsForm()
                connection_form = ConnectionForm()
                template = 'productivity/network.html'
            # phrase see how many connections have and /10 and then i got level and curnet 
                all_entries = Connections.objects.all()
                lenpeople = len(all_entries)
                level = floor(lenpeople/10)
            return render(request, template, {'connection_form': connection_form,"event_form":event_form,'people':lenpeople,'level':level})
        else:
            connection_form = ConnectionForm()
            event_form = EventsForm()
            template = 'productivity/network.html'
            all_entries = Connections.objects.all()
            lenpeople = len(all_entries)
            level = floor(lenpeople/10)
            return render(request, template, {'connection_form': connection_form,"event_form":event_form,'people':lenpeople,'level':level})
            
    # if a GET (or any other method) we'll create a blank form
    else:
        connection_form = ConnectionForm()
        event_form = EventsForm()
        template = 'productivity/network.html'
        all_entries = Connections.objects.all()
        lenpeople = len(all_entries)
        level = floor(lenpeople/10)
    return render(request, template, {'connection_form': connection_form,"event_form":event_form,'people':lenpeople,'level':level})


def networkdb(request):
    form = ConnectionForm()
    all_entries = Connections.objects.all()
    lenpeople = len(all_entries)
    level = floor(lenpeople/10)
    all_entries = Connections.objects.all()
    template = 'productivity/networkdb.html'
    return render(request, template,{"entries":all_entries,'form': form,'people':lenpeople,'level':level})


def networkevents(request,subj):
    template = 'productivity/networkevents.html'
    all_enteries = NetworkEvents.objects.filter(event_type=subj).order_by('importance')
    # query an object from events and return it to the html in a for loop
    return render(request, template,{'entries':all_enteries,"subj":subj})