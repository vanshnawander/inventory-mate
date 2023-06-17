"""inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    # path('<path:unknown_url>/', views.no_such_url_view, name='no_such_url'),
    path('admin/', admin.site.urls),
    path('', views.home, name='/home'),
    path('login/', views.login, name='login'),
    path('SMhome/', views.SMhome, name='SMhome'),
    path('inentory/', views.inventory, name='inventory'),
    path('createPO/', views.createPO, name='create PO'),
    path('recieverPO/', views.recievePO, name='recievePO.html'),
    path('issues/', views.issues, name='issues'),
    path('sendordertovendor/', views.OrderFinalise,
         name='sending order to vendor'),
    path('home_admin/', views.Home_admin, name='home page admin'),

]
