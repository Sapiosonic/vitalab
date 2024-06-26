# Vitalab

Vitalab é uma aplicação realizada durante o evento PyStack Week 8.0 por Caio Sampaio. O objetivo desse projeto é proporcionar uma visão geral do desenvolvimento de aplicações web utilizando a linguagem de programação Python e o framework Django.

## Guia de instalações:

Instalando o ambiente virtual via powershell:

```
  python -m venv venv
  venv\Scripts\Activate.ps1
```

Instalando as bibliotecas que iremos utilizar no projeto:

```
  pip install django
  pip install pillow
```

Criando um projeto em Django:

```
  django-admin startproject vitalab .
```

Após concluir a instalação do Django, podemos rodar o servidor embutido para testar a instalação, com o seguinte comando:

```
  python manage.py runserver
```

Criar um app:

```
python manage.py startapp <nome_do_app>
```


Criar migrações:

```
python manage.py makemigrations
```

Rodar as migrações:

```
python manage.py migrate
```

Criar um super usuário:

```
python manage.py createsuperuser
```

