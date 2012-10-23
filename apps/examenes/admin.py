from models import *
from django.contrib import admin

class ExamenAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Examen, ExamenAdmin)


