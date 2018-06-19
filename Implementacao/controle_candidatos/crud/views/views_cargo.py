# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from ..dao import *
from ..forms import *
#comando from.. para importar arquivos no diretorio acima do atual
#encontrados em https://stackoverflow.com/questions/12450930/from-import-from-module
#(link acessado no dia 18/06/2018)

#como esclarecido em https://stackoverflow.com/questions/4383571/importing-files-from-different-folder
#adicionar __init__.py faz ser possivel adicionar os arquvios na pasta view
#com comandos do tipo from views import .Link acessado em
#18/06/2018

#inicio das funcoes de create, retrieve, update e delete da tabela Cargo
def novo_cargo(request):
	if request.method == 'POST': #se o usuario quer enviar os dados (clicou em agum botao do tipo enviar)
		dados_cargo = cargo_create_form(request.POST)#vai extrair os dados do formulario para criar cargo que foram enviados pelo usuario
		if dados_cargo.is_valid():
			create_Cargo( dados_cargo.cleaned_data['idCargo'],
							dados_cargo.cleaned_data['nome'],
							dados_cargo.cleaned_data['salario'],
							dados_cargo.cleaned_data['competencias']
						  )
			#referencia para redirect: https://docs.djangoproject.com/en/2.0/topics/http/shortcuts/
			#acessada em 18/06/2018
			return redirect('mostrar_cargo')
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
		if id_cargo.is_valid():#usuario digitou um id que nao eh um inteiro
			delete_cargo(id_cargo.cleaned_data['id_registro'])
			return redirect('mostrar_cargo')
		else:
			mapa_variaveis = {'id_registro':registro_delete_form()}
			return render(request,'crud/exclui_registro.html',mapa_variaveis)	
	else: #usuario carregando/recarregando a pagina
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
			return redirect('mostrar_cargo')
		else:#formulario invalido
			mapa_variaveis = {'form':cargo_create_form()}#mapeia variaveis html com objetos do python
			return render(request,'crud/cargo/update_cargo.html',mapa_variaveis) 
	else:#usuario carregou ou recarregou a pagina
		mapa_variaveis = {'form':cargo_create_form()}#mapeia variaveis html com objetos do python
		return render(request,'crud/cargo/update_cargo.html',mapa_variaveis) 
#fim das funcoes de create, retrieve, update e delete da tabela cargo
def mostra_view_sql(request):
	create_view()
	result_view = show_view()
	destroy_view()
	mapa_variaveis = {'result_view':result_view}#mapeia variaveis html com objetos do python
	return render(request,'crud/cargo/view_sql.html',mapa_variaveis)	

def executa_procedure_sql(request):
	execute_procedure()
	return redirect('mostrar_cargo')
