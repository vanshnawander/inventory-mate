from django.db import models

# Create your models here.
class Product_details(models.Model):
    serial_number=models.IntegerField()
    product_name=models.CharField(max_length=50)
    UOM=models.CharField(max_length=10)
    tax_percentage=models.FloatField()
    price=models.FloatField()
    primary_vendor=models.CharField(max_length=30)
    quantity_available=models.FloatField()


