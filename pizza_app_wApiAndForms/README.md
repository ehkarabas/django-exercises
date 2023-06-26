<div align=center>
	<h1>Pizza APP With API & Forms</h1>
</div>

_Wait a while for the explanatory gif to load..._


<div align="center">
	<img src="./presentation/pizza_app-presentation.gif"/>
</div>

## Description

A simple API system for a pizza app database and the front-end layout of the app, using Django with Django Template Language and Forms. The built-in auth system of Django was used and thus, compared to Django Rest Auth, it made it possible for a user's authentication to remain valid from the time they log in until they log out. The front-end was handled with Bootstrap supported DTL(Django Template Language).

## Goals

Practicing on models, field types, Django Template Language(DTL), creating custom templates, Django Forms, model forms, function based views with forms & templates, using csrf token on templates to provide source control(at the same time prevent a django error based on csrf token), context dictionaries, class based generic display(list & detail) and generic editing(create & update & delete) views with forms & templates, redirecting via success_url class attribute on class based views, overriding post method of BaseCreateView & BaseUpdateView on CreateView & UpdateView class views to use Django messages with views, overriding get method on DeleteView class view not to use a template while deletion in process, accessing related model fields directly via context on templates of ListView & DetailView views, accessing related model fields via building url query on template(home.html) & processes of get_context_data on CreateView view, creating auth views based on django built-in auth system, building a message infrastructure on base.html to display specified message on layout if request has Django messages, using a setTimeout function via external script that imported at the end of base.html's body to show messages for a specific time, extending templates from pre-defined base.html, building static & media dirs on settings.py & project.urls.py to store css files of templates & images uploaded by end-user to model fields, displaying forms as HTML tables on HTML as they are by default, using custom template names on generic class based views, redirecting to detail & update & delete links & navbar links via html a(anchor) elements.

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
pizza_app_wApiAndForms(folder)
|
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
├── media
│   └── pizza_pics
│       ├── pizza1.jpeg
│       ├── pizza2.jpg
│       └── pizza3.jpg
├── pizza
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-311.pyc
│   │       └── __init__.cpython-311.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-311.pyc
│   │   ├── apps.cpython-311.pyc
│   │   ├── forms.cpython-311.pyc
│   │   ├── __init__.cpython-311.pyc
│   │   ├── models.cpython-311.pyc
│   │   ├── urls.cpython-311.pyc
│   │   └── views.cpython-311.pyc
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── presentation
│   └── pizza_app-presentation.gif
├── README.md
├── requirements.txt
├── static
│   ├── css
│   │   └── style.css
│   ├── images
│   │   ├── coolslice.png
│   │   └── pizzabackground.jpg
│   └── js
│       └── timeout.js
├── templates
│   ├── base.html
│   ├── home.html
│   ├── pizza
│   │   ├── order_detail.html
│   │   ├── order_form.html
│   │   └── order_list.html
│   └── user
│       └── user_form.html
└── user
    ├── admin.py
    ├── apps.py
    ├── forms.py
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
    │   ├── urls.cpython-311.pyc
    │   └── views.cpython-311.pyc
    ├── tests.py
    ├── urls.py
    └── views.py
```