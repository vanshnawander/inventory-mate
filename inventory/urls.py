from django.contrib import admin
from django.urls import path
from myapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('<path:unknown_url>/', views.no_such_url_view, name='no_such_url'),
    path('admin/', admin.site.urls),
    #path('', views.SMhome, name='SMhome'),
    path('', views.login_view, name='login'),
    path('SMhome/', views.SMhome, name='SMhome'),
<<<<<<< HEAD
=======
    path('Mhome/', views.Mhome, name='Mhome'),
>>>>>>> dd9efee4d5d54d44a0ff8b1530dfc7b8888b10ae
    path('inventory/', views.inventory, name='inventory'),
    path('createPO/', views.createPO, name='create PO'),
    path('recieverPO/', views.recievePO, name='recievePO.html'),
    path('issues/', views.issues, name='issues'),
    path('sendordertovendor/', views.OrderFinalise,
         name='sending order to vendor'),
    path('home_admin/', views.Home_admin, name='home page admin'),
    path('Addproducts/', views.add_products_in_inventory,
         name='add products in inventory'),
    path('get_dynamic_values/', views.get_dynamic_values, name='get_dynamic_values'),
    path('submit_PO_table/', views.submit_PO_table, name='submit_PO_table'),
]
