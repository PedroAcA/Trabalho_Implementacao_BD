#classe para executar comandos sql e acessar o banco de dados
from .models import *
from django.db import connection
import base64
nome_app = "crud_"
def retrieve_tabela(nome_tabela):
	with connection.cursor() as con:
		nome_acesso_tabela = nome_app+ nome_tabela
#referencia format extraida em 15/06//2018 de https://stackoverflow.com/questions/34552920/adding-table-name-to-sql-query-at-runtime
		con.execute("SELECT * FROM {}".format(nome_acesso_tabela))
		return con.fetchall()

def create_view():#cria view da tabela cargo com os campos idCargo e nome 
	with connection.cursor() as con:
		con.execute("CREATE VIEW v as SELECT idCargo,nome FROM crud_cargo;")

def show_view():
	with connection.cursor() as con:
		con.execute("SELECT * FROM v")
		result= con.fetchall()
		print result
		return result

def destroy_view():
	with connection.cursor() as con:
		con.execute("DROP VIEW v")	

def execute_procedure():#so chame essa funcao apos ter executado o script procedure.sql
	with connection.cursor() as con:
		con.execute("call teste('x')")
		con.execute("call teste('y')")	

#inicio das funcoes de create, delete e update da tabela partido
def create_Partido(idPartido,nome,sede,nomePresidente,qtdFiliados,dataCriacao):
	with connection.cursor() as con:
#referencia para inserir os dados formatados na string retirada de 
#https://www.learnpython.org/en/String_Formatting em 16/06/2018

		con.execute( "INSERT INTO crud_partido"+
					 " VALUES (%s,'%s','%s','%s',%s,'%s')"%(idPartido,nome,sede,nomePresidente,qtdFiliados,dataCriacao)
				   )

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
#fim das funcoes de create, delete e update da tabela partido

#inicio das funcoes de create, delete e update da tabela cargo
def create_Cargo(idCargo,nome,salario,competencias):
	with connection.cursor() as con:
#referenciapara inserir os dados formatados na string retirada de 
#https://www.learnpython.org/en/String_Formatting em 16/06/2018
		con.execute("INSERT INTO crud_cargo"+
					" VALUES (%s,'%s',%s,'%s')"%(idCargo,nome,salario,competencias)
				   )

def delete_cargo(idCargo):
	with connection.cursor() as con:
		con.execute("DELETE FROM crud_cargo WHERE idCargo = %s"%(idCargo))

def update_cargo(idCargo,nome,salario,competencias):
	with connection.cursor() as con:
#referenciapara inserir os dados formatados na string retirada de 
#https://www.learnpython.org/en/String_Formatting em 16/06/2018
		con.execute("UPDATE crud_cargo"
					+
					" SET nome='%s',salario=%s,competencias='%s'"%(nome,salario,competencias)
				    +
				    " WHERE idCargo= %s"%(idCargo)
				   )
#fim das funcoes de create, delete e update da tabela cargo

#inicio das funcoes de create, delete e update da tabela politico
def create_Politico(idPolitico,nome,apelido,foto,idPartido,idCargo):
	with connection.cursor() as con:
#referenciapara inserir os dados formatados na string retirada de 
#https://www.learnpython.org/en/String_Formatting em 16/06/2018
#referencia para base64.b64encode extraida de https://code.tutsplus.com/tutorials/base64-encoding-and-decoding-using-python--cms-25588
#em 17/06/2018
		con.execute("INSERT INTO crud_politico"+
					" VALUES (%s,'%s','%s','%s',%s,%s)"%(idPolitico,nome,apelido,base64.b64encode(foto.read()),idPartido,idCargo)
				   )

def delete_politico(idPolitico):
	with connection.cursor() as con:
		con.execute("DELETE FROM crud_politico WHERE idPolitico = %s"%(idPolitico))

def update_politico(idPolitico,nome,apelido,foto,idPartido,idCargo):
	with connection.cursor() as con:
#referenciapara inserir os dados formatados na string retirada de 
#https://www.learnpython.org/en/String_Formatting em 16/06/2018
		con.execute("UPDATE crud_politico"
					+
					" SET nome='%s',apelido='%s',foto='%s',idPartido_id=%s,idCargo_id=%s"%(nome,apelido,base64.b64encode(foto.read()),idPartido,idCargo)
				    +
				    " WHERE idPolitico= %s"%(idPolitico)
				   )
#fim das funcoes de create, delete e update da tabela politico
