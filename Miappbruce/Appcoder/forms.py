from django import forms



class createNewCliente(forms.Form):
    Nombre = forms.CharField(label='nombre',max_length=100)
    Apellido = forms.CharField(max_length=100)
    email = forms.EmailField()
    
    
class createNewProducto(forms.Form):
    Nombre = forms.CharField(label='nombre',max_length=100)
    categoria =forms.CharField(widget=forms.Textarea)
   
   
class createNewRh(forms.Form):
    Nombre = forms.CharField(label='nombre',max_length=100)
    Area = forms.CharField(label='Area',max_length=100)