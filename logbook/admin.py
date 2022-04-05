from django.contrib import admin
from .models import *



# Register your models here.
@admin.register(Logbook)
class LogbookAdmin(admin.ModelAdmin):
    list_display = ['driver']


@admin.register(LogbookEntry)
class LogbookEntryAdmin(admin.ModelAdmin):
    list_display = ['date', 'logbook', 'total_hours']
