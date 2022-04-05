from django.db import models
from django.forms import TimeField

from loads.models import Driver

# Create your models here.
class Logbook(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.driver.name

class LogbookEntry(models.Model):
    date = models.DateField()
    truck_no = models.IntegerField(blank=True, null=True)
    pickup_address= models.TextField(blank=True, null=True)
    time_in = models.TimeField(blank=True, null=True)
    time_out = models.TimeField(blank=True, null=True)
    delivery_address = models.TextField(blank=True, null=True)
    delivery_timein = models.TimeField(blank=True, null=True)
    delivery_timeout = models.TimeField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    driving_hours = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    total_hours = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    logbook = models.ForeignKey(Logbook, on_delete=models.PROTECT)

    class Meta:
        ordering = ['id']