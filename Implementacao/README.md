Sera utilizada django(versao 1.11.1) + pesquisa com comandos sql (em django) para implementar o crud
Estrutura da pasta de implementação:

		->SQL_controle_candidatos_mysqlworkbench.sql: arquivo com os comandos sql gerados automaticamente pelo MySQLworkbench para o modelo relacional presente na pasta Projetos/MR do repositório

		->controle_candidatos: pasta contendo os apps em Django para fazer as funções de Create Retrieve Update e Delete (CRUD)

		->comentarios_sobre_procedure.txt: arquivo com referencias (links) sobre como utilizar.


		->criar_banco_dados.sql: arquivo com o comando sql para criar o banco de dados utilizado pelo programa. Cria um banco vazio (sem tabelas).


		->instrucoes_para_criar_banco_dados.txt: arquivo com instruções para configurar o MySQL no Django e para criar o banco de dados vazio sem utilizar comandos SQL. As instruções para criar o banco vazio também estão descritas abaixo nesse documento.  

		->procedure.sql: arquivo sql com comando para criar uma procedure

		->drop.sql: arquivo sql com comando para apagar o banco de dados e a procedure se esses existirem

		->diagrama_acesso_bd.png:imagem que contém o diagrama apresentando como a interface gráfica acessa a camada de persistência 


		->README.md: este arquivo

Instruções para instalar o Django encontradas em https://docs.djangoproject.com/en/1.11/topics/install/ (acessado no dia 16/06/2018)

Devido ao uso do Sistema Gerenciador de Banco de Dados (SGBD) MySQL, o comando abaixo deve ser executado em terminal para criar o banco de dados necessário à utilizacao do projeto:
		
		$ mysql -u root -p <criar_banco_dados.sql

Para maiores instruçoes sobre como configurar o Django para utilizar MySQL, consulte o arquivo 'instrucoes_para_criar_banco_dados.txt'.

Se desejar utilizar a procedure de teste, digitar no terminal:

		$ mysql -u root -p crud<procedure.sql

Após instalar o Django e criar o banco de dados, abrir o terminal na pasta controle_candidatos/ (a que possui o arquivo manage.py) e executar os seguintes comandos de terminal:
		
		$ python manage.py makemigrations crud

		$ python manage.py migrate 

		$ python manage.py runserver

Esses comandos vão, respectivamente, transformar o modelo relacional em um sql (caso não tenho sido feito ainda), criar as tabelas do banco de dados e iniciar o servidor. Para usar o crud, va ate 'http://127.0.0.1:8000' e escolha uma das opções que se localizam na parte superior da página. 
		
Se desejar ver o sql gerado pelo django, digitar no terminal: 

		$ python manage.py sqlmigrate crud 0001

Se desejar apagar o banco de dados e a procedure em conjunto, digitar no terminal:
		$ mysql -u root -p crud<drop.sql

