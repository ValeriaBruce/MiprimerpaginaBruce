from django.template import Template, Context
from django.http import HttpResponse   

def probandoTemplate (self):

    miHtml= open ("C:/Users/bruce/OneDrive/Escritorio/Miproyecto/Miappbruce/template/prueba.html")

    plantilla= Template (miHtml.read())

    miHtml.close()

    micontexto= Context()

    documento= plantilla.render (micontexto)

    return HttpResponse (documento)