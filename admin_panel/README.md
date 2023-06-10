<div align=center>
	<h1>Django Admin Panel</h1>
</div>

_Wait a while for the explanatory gif to load..._


<div align="center">
	<img src="./presentation/admin_panel-presentation.gif"/>
</div>

## Description

Own customized Django Admin Panel and a Django Admin Interface listed on django.org.

## Goals

Practicing on custom model layout, filter by date ribbon, custom model actions dropdown, read only model fields on model layout, thumbnail images(belongs to ImageField) on model layout, custom filter dropdowns on model layout, import/export feature on models, custom instance layout, custom sized read only images(belongs to ImageField) on instance layout, listing related foreign table rows in instance, customizing admin panel on desire from scratch via overriding templates on env/lib/django/contrib/admin/templates/admin, grapelli.

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
admin_panel(folder)
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
│   └── ehlogo.png
├── presentation
│   └── admin_panel-presentation.gif
├── product
│   ├── admin.py
│   ├── apps.py
│   ├── faker.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_product_description.py
│   │   ├── 0003_review.py
│   │   ├── 0004_category_product_categories.py
│   │   ├── 0005_product_image.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-311.pyc
│   │       ├── 0002_alter_product_description.cpython-311.pyc
│   │       ├── 0003_review.cpython-311.pyc
│   │       ├── 0004_category_product_categories.cpython-311.pyc
│   │       ├── 0005_product_image.cpython-311.pyc
│   │       └── __init__.cpython-311.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-311.pyc
│   │   ├── apps.cpython-311.pyc
│   │   ├── faker.cpython-311.pyc
│   │   ├── __init__.cpython-311.pyc
│   │   └── models.cpython-311.pyc
│   ├── tests.py
│   └── views.py
├── requirements.txt
├── static
│   └── ehlogo.png
└── templates
    └── admin
        ├── base_site.html
        └── product
            └── change_form.html
```


