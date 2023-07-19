# from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from myapp.models import Product_details
from myapp.models import Users
from django.db import connection
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.decorators import login_required

def get_dynamic_values(request):
    dependent_value = request.GET.get('dependent_value')
    product_name = dependent_value
    try:
        row = Product_details.objects.get(product_name=product_name)
    except Product_details.DoesNotExist:
        row = None
    
    response = {
        'name': product_name,
        'uom': row.UOM,
        'vendor': row.primary_vendor,
        'price': row.price
    }

    return JsonResponse(response)

@csrf_exempt
def submit_PO_table(request):
    if request.method == 'POST':
        try:
            form_data = json.loads(request.body)
            table_data = form_data['tableData']
            for row in table_data:
                name=row.get("0")
                
            print(table_data)

            return JsonResponse({'message': 'Form data saved successfully.'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)



def no_such_url_view(request, unknown_url):
    return render(request, '404.html', {'unknown_url': unknown_url})

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role =  request.POST['pageSelection']
        try:
            user = Users.objects.get(user_name=username,password=password,role=role)
        except:
            user=None
        if user:
            print("hello")
            return render(request,'PO.html')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html')


def SMhome(request,user):
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
    referer = request.META.get('HTTP_REFERER')
    if not referer:
        return render(request,'404.html')
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


def Home_admin(request,user):
    print(request)
    return render(request, 'ADMINhome.html')

def Mhome(request):
    return render(request, 'Mhome.html')
