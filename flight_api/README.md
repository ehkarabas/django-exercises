<div align=center>
	<h1>Flight API</h1>
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
postlogger_api_client(folder)
|
|-- README.md
|-- api
|   |-- db.sqlite3
|   |-- main
|   |   |-- __init__.py
|   |   |-- __pycache__
|   |   |   |-- __init__.cpython-311.pyc
|   |   |   |-- settings.cpython-311.pyc
|   |   |   |-- urls.cpython-311.pyc
|   |   |   |-- wsgi.cpython-311.pyc
|   |   |-- asgi.py
|   |   |-- settings.py
|   |   |-- urls.py
|   |   |-- wsgi.py
|   |-- manage.py
|   |-- requirements.txt
|   |-- tutorial
|       |-- __init__.py
|       |-- __pycache__
|       |   |-- __init__.cpython-311.pyc
|       |   |-- admin.cpython-311.pyc
|       |   |-- apps.cpython-311.pyc
|       |   |-- models.cpython-311.pyc
|       |   |-- serializers.cpython-311.pyc
|       |   |-- urls.cpython-311.pyc
|       |   |-- views.cpython-311.pyc
|       |-- admin.py
|       |-- apps.py
|       |-- migrations
|       |   |-- 0001_initial.py
|       |   |-- __init__.py
|       |   |-- __pycache__
|       |       |-- 0001_initial.cpython-311.pyc
|       |       |-- __init__.cpython-311.pyc
|       |-- models.py
|       |-- serializers.py
|       |-- tests.py
|       |-- urls.py
|       |-- views.py
|-- client
|   |-- package.json
|   |-- public
|   |   |-- favicon.ico
|   |   |-- index.html
|   |   |-- logo192.png
|   |   |-- logo512.png
|   |   |-- manifest.json
|   |   |-- robots.txt
|   |-- src
|   |   |-- App.js
|   |   |-- components
|   |   |   |-- AddTutorial.jsx
|   |   |   |-- EditTutorial.jsx
|   |   |   |-- TutorialList.jsx
|   |   |-- index.js
|   |   |-- pages
|   |       |-- Home.jsx
|   |-- yarn.lock
|-- presentation
    |-- postlogger_api_client-presentation.gif
```


