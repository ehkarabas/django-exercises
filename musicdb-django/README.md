<div align=center>
	<h1>Music Database Django</h1>
</div>

<div align="center">
	<img src="./presentation/musicdb-django-presentation.gif"/>
</div>

## Description

Simple API system for a basic music database using Django.

## Goals

Practicing on models, field types, table relationships(one-to-one, many-to-one(foreign), many-to-many), rest framework, model serializers, serializermethodfield and primarykeyrelatedfield on serializers, nested serializers, model viewsets, read only modelviewsets, defaultrouter(with basename argument for read only modelviewsets).

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
    $ source env/Scripts/Activate

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
musicdb-django(folder)
|
|-- README.md
|-- db.sqlite3
|-- manage.py
|-- media
|   |-- artists
|   |   |-- acdc.jpg
|   |   |-- acdc_UVzVs8G.jpg
|   |   |-- acdc_iDRGFZE.jpg
|   |   |-- acdc_wwTqEpc.jpg
|   |-- covers
|       |-- razorsedge.jpg
|       |-- razorsedge_ST0TduX.jpg
|-- music_app
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
|   |   |-- __init__.py
|   |   |-- __pycache__
|   |       |-- 0001_initial.cpython-311.pyc
|   |       |-- __init__.cpython-311.pyc
|   |-- models.py
|   |-- serializers.py
|   |-- tests.py
|   |-- urls.py
|   |-- views.py
|-- music_project
|   |-- __init__.py
|   |-- __pycache__
|   |   |-- __init__.cpython-311.pyc
|   |   |-- settings.cpython-311.pyc
|   |   |-- urls.cpython-311.pyc
|   |   |-- wsgi.cpython-311.pyc
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|-- presentation
|   |-- musicdb-django-presentation.gif
|-- requirements.txt
```


