
from django import forms
subjects =(
    ("business", "business"),
    ("startups", "startups"),
    ("managment", "managment"),
    ("ai", "ai"),
    ("biohacking", "biohacking")
)

entry_type =(
    ("articles", "article"),
    ("books", "book"),
    ("courses", "course"),
    ("others", "other"),
    )
  
event_type=(
    ("meetups", "meetup"),
    ("hakatons", "hakaton"),
    ("conferences", "conference"),
    ("others", "other"),
)
    
class DataForm(forms.Form):
    subjects = forms.ChoiceField(choices = subjects)
    entry_type = forms.ChoiceField(choices = entry_type)
    url = forms.URLField(label='url', max_length=100)
    desc = forms.CharField(label='desc', max_length=100)
    importance =forms.IntegerField(label='value',widget=forms.TextInput(attrs={'placeholder': 'importance'}), max_value=10)

class ConnectionForm(forms.Form):
    full_name = forms.CharField(label='full name',max_length=20)
    contact = forms.CharField(label='contact info',max_length=50)
    title = forms.CharField(label='title', max_length=20)
    desc = forms.CharField(label='desc', max_length=140)
    field = forms.CharField(label='field', max_length=20)

class EventsForm(forms.Form): 
    event_type = forms.ChoiceField(choices = event_type)
    website_name = forms.CharField(label='website name',max_length=50)
    website_url = forms.URLField(label='url')
    importance =forms.IntegerField(label='value',widget=forms.TextInput(attrs={'placeholder': 'importance'}), max_value=10)