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
    path('<path:unknown_url>/', views.no_such_url_view, name='no_such_url'),
    path('admin/', admin.site.urls),
    path('', views.home, name='/home'),
    path('login/', views.login, name='login'),
    path('raiseorder/', views.ProductOrder, name='productorder'),
    path('checkstock/', views.inventory_stock, name='inventory stock'),
    path('modifyorder/', views.OrderAuth, name='modify order'),
    path('sendordertovendor/', views.OrderFinalise,
         name='sending order to vendor'),
    path('home_manager/', views.storemanagerhomepage,
         name='home page for manager'),
    path('home_admin/', views.Home_admin, name='home page admin'),

]
