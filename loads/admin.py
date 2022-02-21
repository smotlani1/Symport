from django.contrib import admin
from .models import *
from datetime import date, timedelta
from .Invoices import InvoiceItem, Customers, Invoices
import openpyxl as xl
from shutil import move

import AutoEmail
from AutoEmail import Email


# Register your models here.

class LoadImageInLine(admin.TabularInline):
    model = LoadImage

@admin.register(Load)
class LoadAdmin(admin.ModelAdmin):
    actions = ["generate_invoices"]
    list_display = ['load_reference']
    search_fields = ['load_reference']
    inlines = [LoadImageInLine]
    
    #Override base queryset to select related foreign key fields for optimization. 
    def queryset(self, request):
        return super(Load, self).get_queryset(request).select_related('invoice').select_related("customer")

    
    @admin.action(description="Create Invoices")
    def generate_invoices(self, request, queryset):
        load_list = list(queryset)

        # Get load object and use it to autpopulate and create invoice with customer, load, and invoice data. Automatically 
        # create directory based on load_reference number. 
        for load in load_list:
            directory = load.customer.name + "/" + load.load_reference
            customer = Customers(load.customer.name, load.customer.street, load.customer.city, load.customer.state, load.customer.zip, load.customer.phone, load.customer.email)
            new_invoice = Invoices(customer)
            new_invoice.add_item(load.load_reference, load.invoice.amount_invoiced, qty=1)
            new_invoice.create_invoice(directory, load.load_reference)
        
        # For loads with created invoices, updates invoice status field to Generated(G) 
        Invoice.objects.filter(id__in=queryset).update(payment_status="G")

        #Move corresponding load images from media folder to associated load_reference named directory. Same
        #folder as invoice. 
        image_list = list(LoadImage.objects.filter(id__in=queryset))
        for image in image_list:
            src_path = "/Users/sm/Desktop/comp sci/personal projects/symport/media/" + str(image.image)
            dest_path = "/Users/sm/Desktop/Symport/" + image.load.customer.name + "/" + image.load.load_reference
            move(src_path, dest_path)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ['name']


class InvoiceDateFilter(admin.SimpleListFilter):
    title = 'invoice date'
    parameter_name = 'Date'

    def lookups(self, request, model_admin):
        return [
            ('>30', 'Past Due')
        ]

    def queryset(self, request, queryset):
        thirty_days_ago = date.today()-timedelta(days=30)
        if self.value() == '>30':
            return queryset.filter(date__lt=thirty_days_ago)
            
class InvoiceLoadsInLine(admin.TabularInline):
    model = Load
    extra = 0

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceLoadsInLine]
    list_display = ['id']
    list_filter = ['payment_status', InvoiceDateFilter]
    search_fields = ['id']

