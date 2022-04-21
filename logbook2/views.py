from rest_framework.viewsets import *
from django.http import HttpResponse
from django.shortcuts import render
from logbook2.models import LogbookEntry2

from logbook2.serializers import LogbookEntrySerializer

# Create your views here.
class LogbookEntryViewSet(ModelViewSet):
    serializer_class = LogbookEntrySerializer
    # queryset = LogbookEntry.objects.all()

    def get_queryset(self):
        return LogbookEntry2.objects.filter(logbook_id__driver_id=self.request.user.driver.id)