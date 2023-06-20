<div align=center>
	<h1>Stock API</h1>
</div>

_Wait a while for the explanatory gif to load..._


<div align="center">
	<img src="./presentation/stock_api-presentation.gif"/>
</div>

## Description

Simple API system for a stock database using Django as well as authorization API system of the stock database with Django Rest Auth. An auth system has been established, consisting of users with different permission groups, including finance, product, and read-only. A sales record can be created by checking the stock status, and purchase and sale records are appropriately updating the product stock information. DRF auth and custom views are merged and displayed in the DRF template.

## Goals

Practicing on models, field types, and  table relationships(many-to-one(foreign)), user's password hashing on serializers via validate and make_password functions, rest framework, model serializers, stringrelatedfield & primarykeyrelatedfield(to put and post via related table rows' validation) & integerfield on serializers, modelviewsets, django rest auth(login, logout, password reset, user details), showing specific fields to specific users and making a field required at specific request methods via get_fields, password hashing on serializers via update, validate methods and set_password & make_password functions, rest framework token authentication, custom token serializer(for additional "user" field), customized email field on default user model's serializer for unique email rows on database, using custom permission groups via DjangoModelPermissions on views.py and arranging user permission groups on admin panel, determining whether the operation to be performed in a purchase or sale will be an insert or an update & updating the product stock accordingly & displaying this in all related models, checking whether the product stock is sufficient before creating a row in the sale model, requests via DRF template & admin panel, swagger, redoc, debug toolbar.

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
stock_api(folder)
|
├── core
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-311.pyc
│   │   ├── urls.cpython-311.pyc
│   │   └── wsgi.cpython-311.pyc
│   ├── settings
│   │   ├── base.py
│   │   ├── development.py
│   │   ├── __init__.py
│   │   ├── production.py
│   │   └── __pycache__
│   │       ├── base.cpython-311.pyc
│   │       ├── development.cpython-311.pyc
│   │       └── __init__.cpython-311.pyc
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── debug.log
├── manage.py
├── presentation
│   └── stock_api-presentation.gif
├── README.md
├── references
│   ├── stockAPIERD.png
│   └── stockAPI_UserRoles.png
├── requirements.txt
├── stock
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_purchase_quantity_alter_sale_quantity.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-311.pyc
│   │       ├── 0002_alter_purchase_quantity_alter_sale_quantity.cpython-311.pyc
│   │       └── __init__.cpython-311.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-311.pyc
│   │   ├── apps.cpython-311.pyc
│   │   ├── __init__.cpython-311.pyc
│   │   ├── models.cpython-311.pyc
│   │   ├── serializers.cpython-311.pyc
│   │   ├── signals.cpython-311.pyc
│   │   ├── urls.cpython-311.pyc
│   │   └── views.cpython-311.pyc
│   ├── serializers.py
│   ├── signals.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
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


