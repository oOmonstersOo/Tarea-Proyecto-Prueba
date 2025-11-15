from django import forms
from .models import Cliente, Tienda

class ClienteForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    correo = forms.EmailField(label="Correo", required=True)

class TiendaForm(forms.Form):
    nombre = forms.CharField(label='Nombre: ', required=True)
    direccion = forms.CharField(label='Direccion: ', required=True)

class CompraForm(forms.Form):
    fecha = forms.DateField(label='Fecha: ', required=True)
    monto = forms.FloatField(label='Monto: ',required=True)
    cliente = forms.ModelChoiceField(
        queryset = Cliente.objects.all(),
        label="Cliente"
    )
    tienda = forms.ModelChoiceField(
        queryset=Tienda.objects.all(),
        label="Tienda"
    )