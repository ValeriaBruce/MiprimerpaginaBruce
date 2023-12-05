from django.urls import path
from . import views

urlpatterns= [
    path('fecha-actual/',views.mostrar_fecha_actual, name= 'mostrar_fecha_actual'),
    path('Productos/',views.producto_list, name= 'producto'),
    path('Cliente/',views.cliente_list, name='clientes'),
    path('RecursoHumano/',views.RecursoHumano, name='recursoshumanos'),
    path('index/',views.index, name= 'index'),
    path('', views.index), 
    path('about/', views.index2), 
    
]