<div align=center>
	<h1>Rent A Car API</h1>
</div>

_Wait a while for the explanatory gif to load..._


<div align="center">
	<img src="./presentation/rentacar_api-presentation.gif"/>
</div>

## Description

Simple API system for a basic rent a car database using Django as well as authorization API system of the rent a car database with Django Rest Auth. End-users have been provided with the infrastructure to use a real-world rent-a-car API system, where they can specify their reservation start and end dates via URL, and view all vehicles that have not been reserved by other end-users during the dates they have indicated.

## Goals

Practicing on models, field types, and  table relationships(many-to-one(foreign)), user's password hashing on serializers via validate and make_password functions, rest framework, model serializers, stringrelatedfield & integerrelatedfield on serializers, modelviewsets, django rest auth(login, logout, password reset, user details), showing specific fields to specific users and making a field required at specific request methods via get_fields, password hashing on serializers via update, validate methods and set_password, make_password functions, rest framework token authentication, custom token serializer(for additional "user" field), customized email field on default user model's serializer for unique email rows on database, custom permission classes, default authentication classes(to token auth), catching url query parameters via query_params.get, filtering database with field-lookups(gte and lte), using models.Q to mix 'and' & 'or' logic in filter queries, excluding a list queryset(via flat=True argument in values_list), requests via DRF template & admin panel.

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
rentacar_api(folder)
|
├── car
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_rename_started_date_reservation_start_date.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-311.pyc
│   │       ├── 0002_rename_started_date_reservation_start_date.cpython-311.pyc
│   │       └── __init__.cpython-311.pyc
│   ├── models.py
│   ├── permissions.py
│   ├── __pycache__
│   │   ├── admin.cpython-311.pyc
│   │   ├── apps.cpython-311.pyc
│   │   ├── __init__.cpython-311.pyc
│   │   ├── models.cpython-311.pyc
│   │   ├── permissions.cpython-311.pyc
│   │   ├── serializers.cpython-311.pyc
│   │   ├── urls.cpython-311.pyc
│   │   └── views.cpython-311.pyc
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── main
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-311.pyc
│   │   ├── settings.cpython-311.pyc
│   │   ├── urls.cpython-311.pyc
│   │   └── wsgi.cpython-311.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── presentation
│   └── rentacar_api-presentation.gif
├── README.md
├── requirements.txt
└── user
    ├── admin.py
    ├── apps.py
    ├── __init__.py
    ├── migrations
    │   ├── __init__.py
    │   └── __pycache__
    │       └── __init__.cpython-311.pyc
    ├── models.py
    ├── __pycache__
    │   ├── admin.cpython-311.pyc
    │   ├── apps.cpython-311.pyc
    │   ├── __init__.cpython-311.pyc
    │   ├── models.cpython-311.pyc
    │   ├── serializers.cpython-311.pyc
    │   ├── urls.cpython-311.pyc
    │   └── views.cpython-311.pyc
    ├── serializers.py
    ├── tests.py
    ├── urls.py
    └── views.py
```


