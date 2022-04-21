from django.forms import models
from rest_framework import serializers

from .models import LogbookEntry2

class LogbookEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = LogbookEntry2
        fields = ['id','date','truck_no', 'start_time','end_time','driving_hours', 'total_hours', 'logbook']