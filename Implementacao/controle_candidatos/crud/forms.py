#classe para criar as classes com os dados necessarios para as operacoes 
#de create, update e delete
from django import forms
from .forms import *
class partido_create_form(forms.Form):
	idPartido = forms.IntegerField(required=True)
	nome = forms.CharField()
	sede = forms.CharField()
	nomePresidente = forms.CharField()
	qtdFiliados = forms.IntegerField()
	dataCriacao = forms.DateField()

class registro_delete_form(forms.Form):
	id_registro = forms.IntegerField(required=True)
