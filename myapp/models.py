from django.db import models

# Create your models here.
class Product_details(models.Model):
    serial_number = models.IntegerField(unique=True)
    product_name = models.CharField(max_length=50)
    UOM = models.CharField(max_length=10)
    tax_percentage = models.FloatField()
    price = models.FloatField()
    primary_vendor = models.CharField(max_length=30)
    quantity_available = models.FloatField()
    
class list_of_po_iteams(models.Model):
    po_id=models.IntegerField(unique=True)
    product_name=models.CharField(max_length=50)
    product_price=models.FloatField()
    vendor_name=models.CharField(max_length=30)
    time_stamp=models.DateTimeField(auto_now_add=True)
    date=models.DateField(auto_now_add=True)
    quantity=models.IntegerField()
    status=models.CharField(max_length=30)
    user_name=models.CharField(max_length=30)
    
class vendor_details(models.Model):
    vendor_id=models.IntegerField()
    vendor_name=models.CharField(max_length=30)
    vendor_phone=models.IntegerField()

class vendor_price(models.Model):
    vendor_id=models.ForeignKey(vendor_details,on_delete=models.CASCADE)
    product_name=models.ForeignKey(Product_details,on_delete=models.CASCADE)
    product_price=models.FloatField()
    time_stamp=models.DateTimeField(auto_now_add=True)
    
class inventory_in_hand(models.Model):
    product_name=models.CharField(max_length=50)
    quantity=models.IntegerField()
    time_stamp=models.DateTimeField(auto_now_add=True)
    

   
