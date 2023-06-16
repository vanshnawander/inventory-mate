# from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def no_such_url_view(request, unknown_url):
    return render(request, '404.html', {'unknown_url': unknown_url})


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def ProductOrder(request):
    return render(request, 'order.html')


def inventory_stock(request):
    return render(request, 'stock.html')


def OrderAuth(request):
    return render(request, 'orderauth.html')


def OrderFinalise(request):
    return render(request, 'orderFinal.html')


def storemanagerhomepage(request):
    return render(request, 'storemanagerhomepage.html')


def Home_admin(request):
    return render(request, 'home_admin.html')
