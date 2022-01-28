from django.db import models

class Data(models.Model):
    Subjects = models.CharField(max_length=10)
    Entry_type = models.CharField(max_length=10)
    url = models.CharField(max_length=30)
    desc = models.CharField(max_length=30)
    importance = models.IntegerField(max_length=2,default=2)

class Connections(models.Model):
    full_name = models.CharField(max_length=10)
    contact = models.CharField(max_length=10)
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=30)
    field = models.CharField(max_length=30)