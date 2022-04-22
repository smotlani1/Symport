from rest_framework.viewsets import *
from django.http import HttpResponse
from django.shortcuts import render
from logbook2.models import LogbookEntry2, Logbook2

from logbook2.serializers import LogbookEntrySerializer

# Create your views here.
class LogbookEntryViewSet(ModelViewSet):
    serializer_class = LogbookEntrySerializer
    # queryset = LogbookEntry.objects.all()

    
    def get_queryset(self):
        return LogbookEntry2.objects.filter(logbook_id__driver_id=self.request.user.driver.id)

    def perform_create(self, serializer):
        # Save logbook entry post request to correct user 
        x = Logbook2.objects.get(driver_id=self.request.user.driver.id)
        
        serializer.save(logbook=x)