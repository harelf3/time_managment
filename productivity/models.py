from typing_extensions import Required
from django.db import models

class Data(models.Model):
    Subjects = models.CharField(max_length=10)
    Entry_type = models.CharField(max_length=10)
    url = models.CharField(max_length=100)
    desc = models.CharField(max_length=150)
    importance = models.IntegerField(max_length=2,default=2)
    status = models.BooleanField(default=False)

class Connections(models.Model):
    full_name = models.CharField(max_length=10)
    contact = models.CharField(max_length=10)
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=30)
    field = models.CharField(max_length=30)


class NetworkEvents(models.Model):
    event_type = models.CharField(max_length=10)
    website_name = models.CharField(max_length=30)
    website_url = models.CharField(max_length=100)
    importance = models.IntegerField(max_length=2,default=2)


    