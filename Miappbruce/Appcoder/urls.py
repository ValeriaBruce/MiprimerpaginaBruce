from django.urls import path
from . import views

urlpatterns= [
    path('fecha-actual/',views.mostrar_fecha_actual),
    path('Productos/',views.producto_list),
    path('Cliente/',views.cliente_list),
    path('RecursoHumano/',views.RecursoHumano),
    path('index/',views.index),
    
]