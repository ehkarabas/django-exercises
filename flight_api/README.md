<div align=center>
	<h1>Flight API</h1>
</div>

<div align="center">
	<a href="https://ehkarabas.pythonanywhere.com/">
		<img src="https://img.shields.io/badge/live-%23.svg?&style=for-the-badge&logo=www&logoColor=white%22&color=black">
	</a>
</div>

_Wait a while for the explanatory gif to load..._

<div align="center">
	<img src="./presentation/flight_api-presentation.gif"/>
</div>

## Description

Simple API system for a basic flight database using Django as well as authorization API system of the flight database with Django Rest Auth.

## Goals

Practicing on models, field types, table relationships(many-to-one(foreign), many-to-many), rest framework, model serializers, creating a base common model and a serializer and initializing(inheriting) others with them, stringrelatedfield & serializermethodfield & primarykeyrelatedfield on serializers, displaying model field via returning obj.get_fieldName from get_serializerField method, model serializers, overriding modelserializer's create method for non-overridable(many-to-many fields) additional serializer fields, model viewsets, drf-yasg(swagger & redoc), requests via swagger, django rest auth, rest framework token authentication, pagination, default & custom permission classes, default authentication classes, debug-toolbar, different databases & auth_password_validators & debug system & allowed_hosts for differnet deployment types via seperate settings files, connecting & using a postgresql database, requests via postman & rest browser UI & admin panel, defaultrouter.

## Installation

To run this app on your local, run commands below on the terminal:

1. Clone main repo on your local.
    ```shell
    $ git clone https://github.com/ehkarabas/django-exercises.git
    ```

2. Make sure you've installed python and added python to the system path.


3. Install python environment to this sub-repo.
    ```shell
    $ python -m venv env
    ```

4. Activate python environment.
    ```shell
    For powershell:
    $ .\env\Scripts\activate
    
    For git bash:
    $ source env/Scripts/activate

    For linux/mac:
    $ source env/bin/activate
    ```

5. Install required packages to this sub-repo.
    ```shell
    $ python install -r requirements.txt
    ```

6. Run the server on your browser.
    ```shell
    $ python manage.py runserver
    ```



## Resource Structure 

```
flight_api(folder)
|
|-- README.md
|-- core
|   |   |-- __init__.py
|   |   |-- __pycache__
|   |   |-- __init__.cpython-311.pyc
|   |   |-- settings.cpython-311.pyc
|   |   |-- urls.cpython-311.pyc
|   |   |-- wsgi.cpython-311.pyc
|   |-- asgi.py
|   |-- settings
|   |   |-- __init__.py
|   |   |-- __pycache__
|   |   |   |-- __init__.cpython-311.pyc
|   |   |   |-- base.cpython-311.pyc
|   |   |   |-- development.cpython-311.pyc
|   |   |-- production.cpython-311.pyc
|   |   |-- base.py
|   |   |-- development.py
|   |   |-- production.py
|   |-- urls.py
|   |-- wsgi.py
|-- db.sqlite3
|-- flight
|   |-- __init__.py
|   |-- __pycache__
|   |   |-- __init__.cpython-311.pyc
|   |   |-- admin.cpython-311.pyc
|   |   |-- apps.cpython-311.pyc
|   |   |-- models.cpython-311.pyc
|   |   |-- serializers.cpython-311.pyc
|   |   |-- urls.cpython-311.pyc
|   |   |-- views.cpython-311.pyc
|   |-- admin.py
|   |-- apps.py
|   |-- migrations
|   |   |-- 0001_initial.py
|   |   |-- 0002_alter_reservation_flight_alter_reservation_passenger.py
|   |   |-- __init__.py
|   |   |-- __pycache__
|   |       |-- 0001_initial.cpython-311.pyc
|   |       |-- 0002_alter_reservation_flight_alter_reservation_passenger.cpython-311.pyc
|   |   |-- __init__.cpython-311.pyc
|   |-- models.py
|   |-- serializers.py
|   |-- tests.py
|   |-- urls.py
|   |-- views.py
|-- manage.py
|-- presentation
|   |-- flight_api-presentation.gif
|-- references
|   |-- drawSQL-flightapi-export-2023-05-20.png
|   |-- drawSQL-pgsql-export-2023-05-20.sql
|-- requirements.txt
|-- user
    |-- __init__.py
    |-- __pycache__
    |   |-- __init__.cpython-311.pyc
    |   |-- admin.cpython-311.pyc
    |   |-- apps.cpython-311.pyc
    |   |-- models.cpython-311.pyc
    |   |-- serializers.cpython-311.pyc
    |   |-- urls.cpython-311.pyc
    |   |-- views.cpython-311.pyc
    |-- admin.py
    |-- apps.py
    |-- migrations
    |   |-- __init__.py
    |   |-- __pycache__
    |   |-- __init__.cpython-311.pyc
    |-- models.py
    |-- serializers.py
    |-- tests.py
    |-- urls.py
    |-- views.py
```

