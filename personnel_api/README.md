<div align=center>
	<h1>Personnel API</h1>
</div>

_Wait a while for the explanatory gif to load..._


<div align="center">
	<img src="./presentation/personnel_api-presentation.gif"/>
</div>

## Description

Simple API system for a basic personnel database using Django as well as authorization API system of the personnel database with Django Rest Auth.

## Goals

Practicing on models, field types, table relationships(one-to-one, many-to-one(foreign)), rest framework, model serializers, stringrelatedfield & serializermethodfield & primarykeyrelatedfield on serializers, generic concrete views, django rest auth, rest framework token authentication, custom permission classes, default authentication classes, signals to create a model instance and token simultanously for the newly created related user, removing user's token via additional view & endpoint, requests via postman & rest browser UI & admin panel.

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
personnel_api(folder)
|
|-- README.md
|-- db.sqlite3
|-- main
|   |   |-- __init__.py
|   |   |-- __pycache__
|   |   |-- __init__.cpython-311.pyc
|   |   |-- settings.cpython-311.pyc
|   |   |-- urls.cpython-311.pyc
|   |   |-- wsgi.cpython-311.pyc
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|-- manage.py
|-- media
|   |-- images
|       |-- avatar.png
|-- personnel
|   |-- __init__.py
|   |-- __pycache__
|   |   |-- __init__.cpython-311.pyc
|   |   |-- admin.cpython-311.pyc
|   |   |-- apps.cpython-311.pyc
|   |   |-- models.cpython-311.pyc
|   |   |-- permissions.cpython-311.pyc
|   |   |-- serializers.cpython-311.pyc
|   |   |-- urls.cpython-311.pyc
|   |   |-- views.cpython-311.pyc
|   |-- admin.py
|   |-- apps.py
|   |-- migrations
|   |   |-- 0001_initial.py
|   |   |-- 0002_alter_personnel_started_date.py
|   |   |-- __init__.py
|   |   |-- __pycache__
|   |       |-- 0001_initial.cpython-311.pyc
|   |       |-- 0002_alter_personnel_department_id.cpython-311.pyc
|   |       |-- 0002_alter_personnel_started_date.cpython-311.pyc
|   |   |-- __init__.cpython-311.pyc
|   |-- models.py
|   |-- permissions.py
|   |-- serializers.py
|   |-- tests.py
|   |-- urls.py
|   |-- views.py
|-- presentation
|   |-- personnel_api-presentation.gif
|-- project_requirements.txt
|-- requirements.txt
|-- users
    |-- __init__.py
    |-- __pycache__
    |   |-- __init__.cpython-311.pyc
    |   |-- admin.cpython-311.pyc
    |   |-- apps.cpython-311.pyc
    |   |-- models.cpython-311.pyc
    |   |-- serializers.cpython-311.pyc
    |   |-- signals.cpython-311.pyc
    |   |-- urls.cpython-311.pyc
    |   |-- views.cpython-311.pyc
    |-- admin.py
    |-- apps.py
    |-- migrations
    |   |-- 0001_initial.py
    |   |-- __init__.py
    |   |-- __pycache__
    |       |-- 0001_initial.cpython-311.pyc
    |   |-- __init__.cpython-311.pyc
    |-- models.py
    |-- serializers.py
    |-- signals.py
    |-- tests.py
    |-- urls.py
    |-- views.py
```


