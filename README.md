# Desafio Teros
## Tema: Open Banking
  
Sob a proposta do desenvolvimento de um módulo de aplicação que apresentasse uma lista de todos os participantes do Open Banking (extraídos do link: : https://data.directory.openbankingbrasil.org.br/participants) e exibição dos nomes, logos e URLs de configuração/discovery de seus Authorizations Servers, foi desenvolvida uma aplicação utilizando o framework Django 3.2.9 tanto para o frontend (templates) como para o backend (views e models), com auxílio de Python 3.9.5.  
  
Foi utilizado um banco de dados em SQLite, e também foi utilizado Django-q e Redis para realizarem-se atualização assíncronas no banco de dados de 5 em 5 minutos.  
  
Para instalar e rodar este módulo, é necessário clonar este repositório localmente, instalar as dependências necessárias através do pipenv e então rodar os arquivos batch MAKEMIGRATIONS_AND_MIGRATE.bat e em seguida executar os arquivos batch RUN_DJANGO.bat e RUN_WORKERS.bat. Com isso, o módulo desenvolvido estará promto para ser utilizado localmente, através do seu browser de preferência ao acessar seu localhost.
