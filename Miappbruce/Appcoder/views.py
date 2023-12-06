from django.shortcuts import render ,redirect
from django.http import HttpResponse
import datetime
from .models import Producto, Cliente, RecursoHumano
from .forms import createNewCliente ,createNewProducto,createNewRh


def producto(request):
      productos = Producto.objects.all()
      return render (request,'producto.html',{
        'productos':productos
    })

def cliente(request):
    clientes = Cliente.objects.all()
    return render (request,'cliente.html',{
        'clientes':clientes
    })

def rh(request):
    rrhh = RecursoHumano.objects.all()
    return render (request,'rh.html',{
        'rrhh': rrhh
    })


def index(request):
    return render(request,'index.html')

def crearCliente(request):
   if request.method=='GET':
    return render(request,'crearCliente.html', {
        'form':createNewCliente
    })
   else:
    Cliente.objects.create( Nombre=request.POST['Nombre'] ,Apellido=request.POST['Apellido'],email=request.POST['email'])

    return redirect('/Cliente/')

def crearProducto(request):
   if request.method=='GET':
    return render(request,'crearProducto.html', {
        'form':createNewProducto
    })
   else:
    Producto.objects.create( Nombre=request.POST['Nombre'] ,categoria=request.POST['categoria'])

    return redirect('/producto/')


def crearRh(request):
   if request.method=='GET':
    return render(request,'crearRh.html', {
        'form':createNewRh
    })
   else:
    RecursoHumano.objects.create( Nombre=request.POST['Nombre'] ,Area=request.POST['Area'])

    return redirect('/rh/')