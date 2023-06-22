<div align=center>
	<h1>Task Tracker API With Forms</h1>
</div>

_Wait a while for the explanatory gif to load..._


<div align="center">
	<img src="./presentation/task_tracker_api-presentation.gif"/>
</div>

## Description

Simple API system for a task tracker database using Django with Django Template Language and Forms. 

## Goals

Practicing on models, field types, Django Template Language(DTL), creating custom templates, Django Forms, model forms, function based views with forms & templates, using csrf token on templates to provide source control(at the same time prevent a django error based on csrf token), using different logic on function based views if request type is POST, context dictionaries, redirecting via redirect function on function based views, class based generic display(list & detail) and generic editing(create & update & delete) views with forms & templates, redirecting via success_url class attribute on class based views, overriding post method of BaseCreateView & BaseUpdateView & BaseDeleteView on CreateView & UpdateView & DeleteView class views to use Django messages with views, overriding get method on DeleteView class view, rest framework token authentication, building a message infrastructure on base.html to display specified message on layout if request has Django messages, extending templates from pre-defined base.html, displaying forms as HTML tables on HTML as they are by default, using default template names according to specific generic class based views, redirecting to detail & update & delete links via html a(anchor) element in table td elements.

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
task_tracker_apiWform(folder)
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
├── presentation
│   └── task_tracker_api-presentation.gif
├── README.md
├── requirements.txt
├── templates
└── todo
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── __init__.py
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── __init__.py
    │   └── __pycache__
    │       ├── 0001_initial.cpython-311.pyc
    │       └── __init__.cpython-311.pyc
    ├── models.py
    ├── __pycache__
    │   ├── admin.cpython-311.pyc
    │   ├── apps.cpython-311.pyc
    │   ├── forms.cpython-311.pyc
    │   ├── __init__.cpython-311.pyc
    │   ├── models.cpython-311.pyc
    │   ├── urls.cpython-311.pyc
    │   └── views.cpython-311.pyc
    ├── templates
    │   ├── add.html
    │   ├── add_update.html
    │   ├── base.html
    │   ├── list.html
    │   ├── todo
    │   │   ├── todo_confirm_delete.html
    │   │   ├── todo_detail.html
    │   │   ├── todo_form.html
    │   │   └── todo_list.html
    │   └── update.html
    ├── tests.py
    ├── urls.py
    └── views.py
```