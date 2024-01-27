# DRF Python cadastro Login Produtos feito com DRF
*DOCKER
*cadastro usuarios, *cadastro avatar relacao one to one com usuario, *cadastro produto relacao onte to many com usuario
*login, token, *refresh token
Api feita com Python e usando o framework django-rest-framework, api com cadastro de usuários, login, mysql , relação onte - to - one , many to many e cadastro de produtos por usuário

**********************

rodar com Docker

*no .env configure o banco de dados -> host tem que ser 'db'

* 1 crie a tabela no banco de dados
  
* terminal -> docker-compose up -d db

------------------------------------------------
* agora crie um banco de dados 

- docker exec -it mysql-container bash

- mysql -u root -p

- -> digite a senha do seu banco

-CREATE DATABASE python_login_cadastro_produtos

----------------------------------------------------------------

--ou em uma linha de comando apenas para criar o banco 
->docker exec -i nome_do_seu_container_mysql mysql -u seu_usuario -pseu_senha -e "CREATE DATABASE nome_do_seu_banco;"

-----------------------------------------------------------------------

* terminal -> docker-compose stop db

* agora rode -> docker-compose up -d

* para parar -> docker-compose down

* agora rode td docker-compose up -d

*************************

rodar com comando Python DRF

* confgure o .env host tem que ser localhost

* crie o banco de dados nome -> python_login_cadastro_produtos

*  .\venv\Scripts\activate 

* pip install -r requirements.txt

* python manage.py makemigrations   

* python manage.py migrate 

* python manage.py runserver 

