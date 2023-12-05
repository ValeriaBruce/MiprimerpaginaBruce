from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Producto, Cliente, RecursoHumano

def mostrar_fecha_actual(request):
    fecha_actual= datetime.datetime.now()
    return render(request,'fecha_actual.html', {'fecha_actual':fecha_actual})

def producto_list(request):
    productos= Producto.objects.all()
    print(productos)
    return render (request,'producto_list.html',{'productos':productos} )

def cliente_list(request):
    cliente= cliente.objects.all()
    print(cliente)
    return render (request,'cliente_list.html',{'cliente':cliente})


def index(request):
    return render(request,'index.html')

def index2(request):
    return HttpResponse('<h1>hola walter<h1>')