from django.contrib import admin
from .models import *



# Register your models here.
@admin.register(Logbook2)
class LogbookAdmin(admin.ModelAdmin):
    list_display = ['driver']


@admin.register(LogbookEntry2)
class LogbookEntryAdmin(admin.ModelAdmin):
    list_display = ['date', 'logbook', 'total_hours']
