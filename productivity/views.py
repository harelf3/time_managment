from tempfile import template
from tkinter import Entry
from django.shortcuts import render
from django.http import HttpResponse
from math import floor
from django.urls import reverse

# Create your views here.

def index(request):
    template = 'productivity/index.html'
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
            knowledge = Data.objects.all()
            lenknowledge = len(knowledge)
            level = floor(lenknowledge/10)
            return render(request, 'productivity/knowledge.html', {'form': form,'knowledge':lenknowledge,'level':level})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DataForm()
        knowledge = Data.objects.all()
        lenknowledge = len(knowledge)
        level = floor(lenknowledge/10)
    return render(request, 'productivity/knowledge.html', {'form': form,'knowledge':lenknowledge,'level':level})


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

def knowledgeresources(request,subj,type):
    if request.method == 'POST':
        value=request.POST['entry_data']
        Data.objects.filter(id=value).update(status=True)
        template = 'productivity/knowledgeresources.html'
        all_enteries = Data.objects.filter(Subjects=subj,Entry_type=type).order_by('importance')
        # query an object from events and return it to the html in a for loop
        return render(request, template,{'entries':all_enteries,"subj":subj,'type':type})
    else:
        template = 'productivity/knowledgeresources.html'
        all_enteries = Data.objects.filter(Subjects=subj,Entry_type=type).order_by('importance')
        # query an object from events and return it to the html in a for loop
        return render(request, template,{'entries':all_enteries,"subj":subj,'type':type})


def player(request):
    template = 'productivity/youtubeplayer.html'
    return render(request,template)

def emailsender(request):
    import smtplib, ssl

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "bikurofepy@gmail.com"  # Enter your address
    receiver_email = "alonlalon123@gmail.com"  # Enter receiver address
    password = "e98vv734"

    knowledge_info = """<h1>KnowLedge</h1>\n"""
    for subj in ["business","startups","managment","ai","biohacking"]:
        data = Data.objects.filter(Subjects =subj)
        if data :
            knowledge_info = knowledge_info + "<h2>"+ str(subj) +"</h2>" + "\n"
        for entrytype in ["articles","books","courses","others"]:
            catagory = (data.filter(Subjects =subj, Entry_type= entrytype).order_by('importance').reverse())
            if catagory :
                knowledge_info = knowledge_info + "<h3>"+ str(entrytype)+"</h3>" +"\n"
            for i in catagory:
                knowledge_info = knowledge_info + "<br>" +str(i.desc) + " "
                knowledge_info = knowledge_info + str(i.url)
                knowledge_info = knowledge_info 
    connections_info = """<h1>Connections</h1>"""
    for field in ["vcs","software","business","bio","all"]:
        network = Connections.objects.filter(field = field)
        if network :
            connections_info  = connections_info + "<h2>"+ str(field) +"</h2>" 
        if field == "all":
            connections_info = connections_info +"<br>"+ "<h2>All Connections</h2>"
            network = Connections.objects.all()
        for person in network:
                connections_info = connections_info +str(person.full_name) + " "
                connections_info = connections_info + str(person.title) +" "
                connections_info = connections_info + str(person.contact) + " "
                connections_info = connections_info + str(person.desc) + " "
                connections_info = connections_info + str(person.field) + "<br>"

    event_info = """<h1>Events</h1>"""
    for eventtype in ["meetups","hakatons","conferences","others"]:
        data = NetworkEvents.objects.filter(event_type =eventtype).order_by('importance').reverse()
        if data :
            event_info = event_info  +"<h2>"+ str(eventtype) +"</h2>" 
        for event in data:
                event_info = event_info + str(event.website_name) + " "
                event_info = event_info + str(event.website_url) + "<br>"


    events = NetworkEvents.objects.all()
    print(events)

    from email.message import EmailMessage
    msg = EmailMessage()
    msg['Subject'] = 'Here Is Your Summary'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content('''
    <!DOCTYPE html>
    <html>
        <body>
            <h1>Efficency summary</h1>
            <br></br>
    
            '''+ knowledge_info +'''
            '''+ connections_info +'''
            '''+ event_info +'''
            <br><b>Have A WonderFull Day.</b></br>
        </body>
    </html>
    ''', subtype='html')


    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.send_message(msg)
    return HttpResponseRedirect(reverse('index'))