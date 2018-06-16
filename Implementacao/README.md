Sera utilizada django(versao 1.11.1) + pesquisa com comandos sql (em django) para implementar o crud
Estrutura da pasta de implementação:
		->SQL_controle_candidatos.sql: arquivo com os comandos sql gerados automaticamente pelo MySQLworkbench para o modelo relacional presente na pasta Projetos/MR do repositório
		->controle_candidatos: pasta contendo os apps em Django para fazer as funções de Create Retrieve Update e Delete (CRUD)

Instruções para instalar o Django encontradas em https://docs.djangoproject.com/en/1.11/topics/install/ (acessado no dia 16/06/2018)

Após instalar o Django, abrir o terminal na pasta controle_candidatos/ (a que possui o arquivo manage.py) e executar os seguintes comandos de terminal:
		$ python manage.py makemigrations crud
		$ python manage.py migrate
		$ python manage.py runserver
Esses comandos vão, respectivamente, transformar o modelo relacional em um sql (caso não tenho sido feito ainda), criar o banco de dados e iniciar o servidor. Para usar o crud, digite no seu navegador web apos o runserver uma das seguintes urls:
		http://127.0.0.1:8000/crud/lista_partido/ 
		http://127.0.0.1:8000/crud/novo_partido/
		http://127.0.0.1:8000/crud/exclui_partido/
		http://127.0.0.1:8000/crud/atualiza_partido/

Se desejar ver o sql gerado pelo django, digitar no terminal: 

		$ python manage.py sqlmigrate crud 0001
