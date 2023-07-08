from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    # path('<path:unknown_url>/', views.no_such_url_view, name='no_such_url'),
    path('admin/', admin.site.urls),
    path('', views.SMhome, name='SMhome'),
    path('login/', views.login, name='login'),
    path('SMhome/', views.SMhome, name='SMhome'),
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
