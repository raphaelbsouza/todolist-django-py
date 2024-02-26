Criando Projeto em Django:

*(Biblioteca Django)*

Criando Ambiente Virtual:

- python -m venv .venv | (.venv pode ser qualquer name.)

Verificando Permissão PowerShell:

- Get-ExecutionPolicy
- Set-ExecutionPolicy -Scope Process -ExecutinPolicy ByPass

Ativar Ambiente Virtual VENV, Virtual Enviroument.

- .\.venv\Scripts\activate 

Criando Projeto - setup = nome do projeto:
- django-admin startproject setup .

Abrindo o Projeto:
- python manage.py runserver

Criando todos, todos = Nome do Projeto;
- python manage.py startapp todos

========================

manage.py = Arquivo Principal do Django:

O que significa cada Arquivo .py dentro da Pasta /setup? 

__init__ = Arquivo de Inicialização do Python

settings.py = Arquivo de Configuração Principal do django

urls.py = Rotas do localhost

wsgi e asgi = 
wsgi = Arquivo para envio de arquivos para este padrão do Python

asgi = Programação assíncrona.

admin.py | Arquivo de Configuração do Administrador do Sistema.

MTV 
=
Model, Template, View

Model = Relacionada a Banco de Dados.

Classes em python para representar as tarefas no banco.

Template = Camada de Interação / arquivos de template html

View = Camada do que a aplicação irá realizar.

===========

 python .\manage.py makemigrations

 Criando uma Migração, Versionamento do Banco de dados.


python .\manage.py migrate

==========
Criando Segurança no Projeto.
Biblioteca Python decouple
=

pip install python-decouple 


=======
Biblioteca dj-database-url
Conversão:
pip install dj-database-url

Formatação path:
pip install black