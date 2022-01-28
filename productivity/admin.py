from django.contrib import admin


from .models import Data
from .models import Connections

admin.site.register(Data)
admin.site.register(Connections)