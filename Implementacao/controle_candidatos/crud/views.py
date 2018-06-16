# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from dao import *
from django.shortcuts import render
from forms import *

# Create your views here.
#inicio das funcoes de create e update da tabela partido
def novo_partido(request):
	if request.method == 'POST': #se o usuario quer enviar os dados (clicou em agum botao do tipo enviar)
		dados_partido = partido_create_form(request.POST)#vai extrair os dados do formulario para criar partido que foram enviados pelo usuario
		if dados_partido.is_valid():
			create_Partido( dados_partido.cleaned_data['idPartido'],
							dados_partido.cleaned_data['nome'],
							dados_partido.cleaned_data['sede'],
							dados_partido.cleaned_data['nomePresidente'],
							dados_partido.cleaned_data['qtdFiliados'],
							dados_partido.cleaned_data['dataCriacao']
						  )
			return HttpResponse("Novo partido adicionado.")
		else:#formulario invalido
			mapa_variaveis = {'form':partido_create_form()}#mapeia variaveis html com objetos do python
			return render(request,'crud/partido/create_partido.html',mapa_variaveis) 
	else:#usuario carregou ou recarregou a pagina
		mapa_variaveis = {'form':partido_create_form()}#mapeia variaveis html com objetos do python
		return render(request,'crud/partido/create_partido.html',mapa_variaveis) 

def mostrar_partido(request):
	lista_partido = retrieve_tabela("partido")
	mapa_variaveis = {'lista_partido':lista_partido}#mapeia variaveis html com objetos do python
	return render(request,'crud/partido/lista_partido.html',mapa_variaveis)

def excluir_partido(request):
	if request.method=='POST':
		id_partido=registro_delete_form(request.POST)
		if id_partido.is_valid():
			delete_Partido(id_partido.cleaned_data['id_registro'])
			return HttpResponse("Partido excluido.")
		else:
			mapa_variaveis = {'id_registro':registro_delete_form()}
			return render(request,'crud/exclui_registro.html',mapa_variaveis)	
	else: #ususario nao digitou um id valido ou etsa carregando/recarregando a pagina
		mapa_variaveis = {'id_registro':registro_delete_form()}
		return render(request,'crud/exclui_registro.html',mapa_variaveis)
#usuario vai ter que preenche todos os dados novamente (para simplificar
#o desenvolvimento visto o pouco tempo restante para desenvolver o crud) 
def atualizar_partido(request):
	if request.method=='POST':
		dados_partido = partido_create_form(request.POST)#vai extrair os dados do formulario para criar partido que foram enviados pelo usuario
		if dados_partido.is_valid():
			update_Partido( dados_partido.cleaned_data['idPartido'],
							dados_partido.cleaned_data['nome'],
							dados_partido.cleaned_data['sede'],
							dados_partido.cleaned_data['nomePresidente'],
							dados_partido.cleaned_data['qtdFiliados'],
							dados_partido.cleaned_data['dataCriacao']
						  )
			return HttpResponse("Partido atualizado.")
		else:#formulario invalido
			mapa_variaveis = {'form':partido_create_form()}#mapeia variaveis html com objetos do python
			return render(request,'crud/partido/update_partido.html',mapa_variaveis) 
	else:#usuario carregou ou recarregou a pagina
		mapa_variaveis = {'form':partido_create_form()}#mapeia variaveis html com objetos do python
		return render(request,'crud/partido/update_partido.html',mapa_variaveis) 
#fim das funcoes de create e update da tabela partido

#inicio das funcoes de create e update da tabela Cargo
def novo_cargo(request):
	if request.method == 'POST': #se o usuario quer enviar os dados (clicou em agum botao do tipo enviar)
		dados_cargo = cargo_create_form(request.POST)#vai extrair os dados do formulario para criar cargo que foram enviados pelo usuario
		if dados_cargo.is_valid():
			create_Cargo( dados_cargo.cleaned_data['idCargo'],
							dados_cargo.cleaned_data['nome'],
							dados_cargo.cleaned_data['salario'],
							dados_cargo.cleaned_data['competencias']
						  )
			return HttpResponse("Novo cargo adicionado.")
		else:#formulario invalido
			mapa_variaveis = {'form':cargo_create_form()}#mapeia variaveis html com objetos do python
			return render(request,'crud/cargo/create_cargo.html',mapa_variaveis) 
	else:#usuario carregou ou recarregou a pagina
		mapa_variaveis = {'form':cargo_create_form()}#mapeia variaveis html com objetos do python
		return render(request,'crud/cargo/create_cargo.html',mapa_variaveis) 

def mostrar_cargo(request):
	lista_cargo = retrieve_tabela("cargo")
	mapa_variaveis = {'lista_cargo':lista_cargo}#mapeia variaveis html com objetos do python
	return render(request,'crud/cargo/lista_cargo.html',mapa_variaveis)

def excluir_cargo(request):
	if request.method=='POST':
		id_cargo=registro_delete_form(request.POST)
		if id_cargo.is_valid():
			delete_cargo(id_cargo.cleaned_data['id_registro'])
			return HttpResponse("Cargo excluido.")
		else:
			mapa_variaveis = {'id_registro':registro_delete_form()}
			return render(request,'crud/exclui_registro.html',mapa_variaveis)	
	else: #ususario nao digitou um id valido ou etsa carregando/recarregando a pagina
		mapa_variaveis = {'id_registro':registro_delete_form()}
		return render(request,'crud/exclui_registro.html',mapa_variaveis)
#usuario vai ter que preenche todos os dados novamente (para simplificar
#o desenvolvimento visto o pouco tempo restante para desenvolver o crud) 
def atualizar_cargo(request):
	if request.method=='POST':
		dados_cargo = cargo_create_form(request.POST)#vai extrair os dados do formulario para criar cargo que foram enviados pelo usuario
		if dados_cargo.is_valid():
			update_cargo( dados_cargo.cleaned_data['idCargo'],
						  dados_cargo.cleaned_data['nome'],
						  dados_cargo.cleaned_data['salario'],
						  dados_cargo.cleaned_data['competencias']
						)
			return HttpResponse("Cargo atualizado.")
		else:#formulario invalido
			mapa_variaveis = {'form':cargo_create_form()}#mapeia variaveis html com objetos do python
			return render(request,'crud/cargo/update_cargo.html',mapa_variaveis) 
	else:#usuario carregou ou recarregou a pagina
		mapa_variaveis = {'form':cargo_create_form()}#mapeia variaveis html com objetos do python
		return render(request,'crud/cargo/update_cargo.html',mapa_variaveis) 
#fim das funcoes de create e update da tabela cargo
