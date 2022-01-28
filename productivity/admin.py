from django.contrib import admin


from .models import Connections,NetworkEvents,Data

admin.site.register(Data)
admin.site.register(Connections)
admin.site.register(NetworkEvents)