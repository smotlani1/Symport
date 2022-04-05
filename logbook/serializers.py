from django.forms import models
from rest_framework import serializers

from .models import LogbookEntry

class LogbookEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = LogbookEntry
        fields = ['id','date','truck_no','pickup_address','time_in','time_out','delivery_address','delivery_timein','delivery_timeout','start_time','end_time','driving_hours', 'total_hours', 'logbook']