from distutils.command.upload import upload
from email.policy import default
from operator import mod
from statistics import mode
from django.db import models
from django.forms import DateTimeField
from django.contrib.auth.models import User
from .SupportingFunctions import get_distance_zips


#This app consists of the following Models: Customer, Driver, Load, Loadimage(images for certain loads)
#and Invoice

#Several string methods overwritten to make admin interface more readable. 

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)

    def __str__(self) -> str:
        return str(self.name)



class Invoice(models.Model):
    #Several status implements to assist with sorting and assisting with the workflow 
    # from load creation to completion and payment
    STATUS_PAID_CHOICES = [
        ('N', "Not Invoiced"),
        ('G', "Generated"),
        ('I', "Invoiced"),
        ('P', "Paid"),
    ]

    date = models.DateField()
    invoice_number = models.IntegerField(null=True)
    amount_invoiced = models.DecimalField(max_digits=7, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=7, decimal_places=2)
    payment_status = models.CharField(max_length=3, choices=STATUS_PAID_CHOICES, default='N')

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    

    def __str__(self) -> str:
        return str(self.id)

class Driver(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)

    user = models.OneToOneField(User, on_delete=models.PROTECT, null=True)


    def __str__(self) -> str:
        return self.name


class Load(models.Model):
    date = DateTimeField()
    start_street = models.CharField(max_length=255)
    start_city = models.CharField(max_length=255)
    start_state = models.CharField(max_length=255)
    start_zip = models.CharField(max_length=255)

    end_street = models.CharField(max_length=255)
    end_city = models.CharField(max_length=255)
    end_state = models.CharField(max_length=255)
    end_zip = models.CharField(max_length=255)

    loaded_distance = models.IntegerField(null=True, blank=True)

    hazmat = models.BooleanField(default=False)

    load_reference = models.TextField(null=True)

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    invoice = models.ForeignKey(Invoice, on_delete=models.PROTECT, related_name="LoadInvoice")
    driver = models.ForeignKey(Driver, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    
    #over ride save method to auto populate  distance using get_distanve function when 
    #adding load information at time of creation
    def save(self, *args, **kwargs):
        self.loaded_distance = get_distance_zips(self.start_zip, self.end_zip)
        super(Load, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.load_reference


class LoadImage(models.Model):
    load = models.ForeignKey(Load, on_delete=models.CASCADE, related_name='loadimage')
    image = models.ImageField(upload_to='loads/images')