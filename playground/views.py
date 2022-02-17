from datetime import date
from django.shortcuts import render
from loads.models import *
from datetime import date, datetime, timedelta
from django.db.models import F, ExpressionWrapper, fields



# Create your views here.
def say_hello(request):
    pass


    return render(request, 'hello.html', {'NotInvoiced': list(queryset)})