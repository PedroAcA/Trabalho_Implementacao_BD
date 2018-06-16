#classe para executar comandos sql e acessar o banco de dados
from .models import *
from django.db import connection
nome_app = "crud_"
def retrieve_tabela(nome_tabela):
	with connection.cursor() as con:
		nome_acesso_tabela = nome_app+ nome_tabela
#referencia format extraida em 15/06//2018 de https://stackoverflow.com/questions/34552920/adding-table-name-to-sql-query-at-runtime
		con.execute("SELECT * FROM [{}] ".format(nome_acesso_tabela))
		return con.fetchall()

def create_Partido(idPartido,nome,sede,nomePresidente,qtdFiliados,dataCriacao):
	with connection.cursor() as con:
#referenciapara inserir os dados formatados na string retirada de 
#https://www.learnpython.org/en/String_Formatting em 16/06/2018
		con.execute("INSERT INTO crud_partido VALUES (%s,'%s','%s','%s',%s,'%s')"%(idPartido,nome,sede,nomePresidente,qtdFiliados,dataCriacao))

def delete_Partido(idPartido):
	with connection.cursor() as con:
		con.execute("DELETE FROM crud_partido WHERE idPartido = %s"%(idPartido))
def update_Partido(idPartido,nome,sede,nomePresidente,qtdFiliados,dataCriacao):
	with connection.cursor() as con:
#referenciapara inserir os dados formatados na string retirada de 
#https://www.learnpython.org/en/String_Formatting em 16/06/2018
		con.execute("UPDATE crud_partido"
					+ 
					" SET nome='%s',sede='%s',nomePresidente='%s',qtdFiliados=%s,dataCriacao='%s'"%(nome,sede,nomePresidente,qtdFiliados,dataCriacao)
					+
					" WHERE idPartido= %s"%(idPartido)
				   )