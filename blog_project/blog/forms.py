from socket import fromshare
from django import forms

class Formulario_productos(forms.Form):

    title = forms.CharField(max_length=250, unique=True)