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

#inicio das funcoes de create, retrieve, update e delete da tabela Politico
def novo_politico(request):
	if request.method == 'POST': #se o usuario quer enviar os dados (clicou em agum botao do tipo enviar)
		dados_politico = politico_create_form(request.POST,request.FILES)#vai extrair os dados do formulario para criar politico que foram enviados pelo usuario
		if dados_politico.is_valid():
			create_Politico( request.POST.get('idPolitico'),
							request.POST.get('nome'),
							request.POST.get('apelido'),
							request.FILES.get('foto'),
							request.POST.get('idPartido'),
							request.POST.get('idCargo')
						  )
			return HttpResponse("Novo politico adicionado.")
		else:#formulario invalido
			mapa_variaveis = {'form':politico_create_form()}#mapeia variaveis html com objetos do python
			return render(request,'crud/politico/create_politico.html',mapa_variaveis) 
	else:#usuario carregou ou recarregou a pagina
		mapa_variaveis = {'form':politico_create_form()}#mapeia variaveis html com objetos do python
		return render(request,'crud/politico/create_politico.html',mapa_variaveis) 

def mostrar_politico(request):
	lista_politico = retrieve_tabela("politico")
	mapa_variaveis = {'lista_politico':lista_politico}#mapeia variaveis html com objetos do python
	return render(request,'crud/politico/lista_politico.html',mapa_variaveis)

def excluir_politico(request):
	if request.method=='POST':
		id_politico=registro_delete_form(request.POST)
		if id_politico.is_valid():
			delete_politico(id_politico.cleaned_data['id_registro'])
			return HttpResponse("Politico excluido.")
		else:
			mapa_variaveis = {'id_registro':registro_delete_form()}
			return render(request,'crud/exclui_registro.html',mapa_variaveis)	
	else: #usuario nao digitou um id valido ou etsa carregando/recarregando a pagina
		mapa_variaveis = {'id_registro':registro_delete_form()}
		return render(request,'crud/exclui_registro.html',mapa_variaveis)
#usuario vai ter que preenche todos os dados novamente (para simplificar
#o desenvolvimento visto o pouco tempo restante para desenvolver o crud) 
def atualizar_politico(request):
	if request.method=='POST':
		dados_politico = politico_create_form(request.POST,request.FILES)#vai extrair os dados do formulario para criar politico que foram enviados pelo usuario
		if dados_politico.is_valid():
			update_politico( request.POST.get('idPolitico'),
							request.POST.get('nome'),
							request.POST.get('apelido'),
							request.FILES.get('foto'),
							request.POST.get('idPartido'),
							request.POST.get('idCargo')
						)
			return HttpResponse("Politico atualizado.")
		else:#formulario invalido
			mapa_variaveis = {'form':politico_create_form()}#mapeia variaveis html com objetos do python
			return render(request,'crud/politico/update_politico.html',mapa_variaveis) 
	else:#usuario carregou ou recarregou a pagina
		mapa_variaveis = {'form':politico_create_form()}#mapeia variaveis html com objetos do python
		return render(request,'crud/politico/update_politico.html',mapa_variaveis) 
#fim das funcoes de create, retrieve, update e delete da tabela Politico