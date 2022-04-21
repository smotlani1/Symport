from django.db import models
from django.forms import TimeField

from loads.models import Driver

# Create your models here.
class Logbook2(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.driver.name

class LogbookEntry2(models.Model):
    date = models.CharField(max_length=255)
    truck_no = models.CharField(max_length=255)
    start_time = models.CharField(max_length=255)
    end_time = models.CharField(max_length=255)
    driving_hours = models.CharField(max_length=255)
    total_hours = models.CharField(max_length=255)
    logbook = models.ForeignKey(Logbook2, on_delete=models.PROTECT)

    class Meta:
        ordering = ['id']