# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from ..dao import *
from django.shortcuts import render
from ..forms import *
#comando from.. para importar arquivos no diretorio acima do atual
#encontrados em https://stackoverflow.com/questions/12450930/from-import-from-module
#(link acessado no dia 18/06/2018)

#como esclarecido em https://stackoverflow.com/questions/4383571/importing-files-from-different-folder
#adicionar __init__.py faz ser possivel adicionar os arquvios na pasta view
#com comandos do tipo from views import .Link acessado em
#18/06/2018

#inicio das funcoes de create, retrieve, update e delete da tabela partido
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
#fim das funcoes de create, retrieve, update e delete da tabela partido