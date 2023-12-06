from django.urls import path
from . import views

urlpatterns= [
    path('', views.index) ,
    path('producto/',views.producto),
    path('Cliente/',views.cliente),
    path('rh/',views.rh),  
    path('crearCliente/',views.crearCliente),
    path('crearProducto/',views.crearProducto),
    path('crearRh/',views.crearRh)
    
]