# from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from myapp.models import Product_details


def no_such_url_view(request, unknown_url):
    return render(request, '404.html', {'unknown_url': unknown_url})


def login(request):
    return render(request, 'login.html',)


def SMhome(request):
    if request.method == 'POST':
        product_name=request.POST['product_name']
        UOM=request.POST['uom']
        tax_percentage=request.POST['tax_percentage']
        price=request.POST['price']
        primary_vendor=request.POST['primary_vendor']
        quantity_available=request.POST['quantity_available']
        table_entry=Product_details(serial_number=1 ,product_name=product_name,UOM=UOM,tax_percentage=tax_percentage,price=price,primary_vendor=primary_vendor,quantity_available=quantity_available)
        table_entry.save()
    a=Product_details.objects.all()
    print(a)
    return render(request, 'SMhome.html',{'Product_details':a})

def add_products_in_inventory(request):
    return render(request, 'additems.html')

def createPO(request):
    return render(request, 'createPO.html')


def recievePO(request):
    return render(request, 'recievePO.html')


def issues(request):
    return render(request, 'issues.html')


def ProductOrder(request):
    return render(request, 'order.html')


def inventory(request):
    return render(request, 'inventory.html')


def OrderFinalise(request):
    return render(request, 'orderFinal.html')


def Home_admin(request):
    return render(request, 'home_admin.html')
