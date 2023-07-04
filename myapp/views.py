# from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from myapp.models import Product_details
from django.db import connection

def no_such_url_view(request, unknown_url):
    return render(request, '404.html', {'unknown_url': unknown_url})


def login(request):
    return render(request, 'login.html',)


def SMhome(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        UOM = request.POST['uom']
        tax_percentage = request.POST['tax_percentage']
        price = request.POST['price']
        primary_vendor = request.POST['primary_vendor']
        quantity_available = request.POST['quantity_available']
        table_entry = Product_details(serial_number=1, product_name=product_name, UOM=UOM, tax_percentage=tax_percentage,
                                      price=price, primary_vendor=primary_vendor, quantity_available=quantity_available)
        table_entry.save()
    a = Product_details.objects.all()
    print(a)
    return render(request, 'SMhome.html', {'Product_details': a})


def add_products_in_inventory(request):
    return render(request, 'additems.html')


def createPO(request):
    query = "SELECT * FROM myapp_Product_details"
    with connection.cursor() as cursor:
        cursor.execute(query)
        items = cursor.fetchall()
        items={i[1]:i[2:] for i in items}
    print(items)
    return render(request, 'createPO.html', {'items':items})


def recievePO(request):
    return render(request, 'recievePO.html')


def issues(request):
    return render(request, 'issues.html')


def ProductOrder(request):
    return render(request, 'order.html')


def inventory(request):
    if request.method == 'POST':
        serial_number = request.POST['serial_number']
        product_name = request.POST['product_name']
        UOM = request.POST['uom']
        tax_percentage = request.POST['tax_percentage']
        price = request.POST['price']
        primary_vendor = request.POST['primary_vendor']
        quantity_available = request.POST['quantity_available']
        par_value = request.POST['par_value']
        table_entry = Product_details(serial_number=1, product_name=product_name, UOM=UOM, tax_percentage=tax_percentage,
                                      price=price, primary_vendor=primary_vendor, quantity_available=quantity_available,
                                      par_value=par_value)
        table_entry.save()
    a = Product_details.objects.all()
    print(a)
    return render(request, 'inventory.html', {'Product_details': a})


def OrderFinalise(request):
    return render(request, 'orderFinal.html')


def Home_admin(request):
    return render(request, 'home_admin.html')
