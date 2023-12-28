<div align=center>
	<h1>DRF With Algolia And Py&JS Clients</h1>
</div>

<div align="center">
      <p>Live API</p>
	<a href="http://drfalgoliapyjsclients.pythonanywhere.com/swagger/">
		<img src="https://img.shields.io/badge/API-%23.svg?&style=for-the-badge&logo=www&logoColor=white%22&color=black">
	</a>
	<hr>
</div>

_You can check the API with this account: username:admin password:admin_

<div align="center">
      <p>You can check presentation as video from below</p>
</div>

[![Go To The Presentation Video](https://i.hizliresim.com/qgmwoyc.png)](https://youtu.be/rz1T2YKJIHM)

<hr>

## Description

An Algolia-indexed Django REST Framework (DRF) database configuration, authenticated with simplejwt and DRF token auth, integrated with JavaScript and Python clients for data transmissions.

## Backend Goals

Practicing on Django, Django Forms, Django Rest Framework, Django Views, DRF Token Authentication, DRF SimpleJWT, DRF JWT Authentication, DRF serializers and model serialziers, creating instance url's with serializers Hyperlinked fields, using custom validators on serializers, using nested serializers to produce more shaped information, overriding DRF serializers' and views' methods, creating custom mixins to spread same permissions to multiple views & change querysets & alter querysets via class attributes & spread request debugging on multiple DRF CBV's, using multiple authentication systems on same project, CRUD operations with DRF functional and generic class views, DRF viewsets and routers, creating custom pagination to put next/previous links on headers, creating custom permissions by request methods on DRF CBV's, customizing model and instance appearances on admin panel, creating python clients for CRUD operations, Creating a JavaScript client to access data requiring authentication using JWT auth, with the capability of automatically refreshing tokens, creating algolia indices on remote via index configuration files, creating algolia client to use with DRF views, creating algolia js clients to use with simple html.

## Technologies

- Django
- DRF
- DRF SimpleJWT
- Algolia

## Installation

To run this app on your local, run commands below on the terminal:

1. Clone main repo on your local.

   ```bash
   git clone https://github.com/ehkarabas/django-exercises.git
   ```

2. Make sure you've installed python and added python to the system path.

3. Install python environment to this sub-repo.

   ```bash
   python -m venv env
   ```

4. Activate python environment.

   4.1. For powershell:

   ```powershell
   .\env\Scripts\activate
   ```

   4.2. For git bash:

   ```bash
   source env/Scripts/activate
   ```

   4.3. For linux/mac:

   ```bash
   source env/bin/activate
   ```

5. Install required packages to this sub-repo.

   ```bash
   python install -r requirements.txt
   ```

6. Run the server on your browser.
   ```bash
   python manage.py runserver
   ```

## Resource Structure

```
drf-w-py-js-clients(folder)
|
├── README.md
├── backend
│   ├── api
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── admin.cpython-312.pyc
│   │   │   ├── apps.cpython-312.pyc
│   │   │   ├── authentication.cpython-312.pyc
│   │   │   ├── faker.cpython-312.pyc
│   │   │   ├── mixins.cpython-312.pyc
│   │   │   ├── models.cpython-312.pyc
│   │   │   ├── permissions.cpython-312.pyc
│   │   │   ├── serializers.cpython-312.pyc
│   │   │   ├── urls.cpython-312.pyc
│   │   │   └── views.cpython-312.pyc
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── authentication.py
│   │   ├── faker.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   │       ├── 0001_initial.cpython-312.pyc
│   │   │       └── __init__.cpython-312.pyc
│   │   ├── mixins.py
│   │   ├── models.py
│   │   ├── permissions.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── articles
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── admin.cpython-312.pyc
│   │   │   ├── apps.cpython-312.pyc
│   │   │   ├── index.cpython-312.pyc
│   │   │   ├── models.cpython-312.pyc
│   │   │   ├── serializers.cpython-312.pyc
│   │   │   ├── urls.cpython-312.pyc
│   │   │   └── views.cpython-312.pyc
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── index.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   │       ├── 0001_initial.cpython-312.pyc
│   │   │       └── __init__.cpython-312.pyc
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── cfehome
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── pagination.cpython-312.pyc
│   │   │   ├── routers.cpython-312.pyc
│   │   │   ├── settings.cpython-312.pyc
│   │   │   ├── urls.cpython-312.pyc
│   │   │   └── wsgi.cpython-312.pyc
│   │   ├── asgi.py
│   │   ├── pagination.py
│   │   ├── routers.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── db.sqlite3
│   ├── manage.py
│   ├── products
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── admin.cpython-312.pyc
│   │   │   ├── apps.cpython-312.pyc
│   │   │   ├── index.cpython-312.pyc
│   │   │   ├── models.cpython-312.pyc
│   │   │   ├── permissions.cpython-312.pyc
│   │   │   ├── serializers.cpython-312.pyc
│   │   │   ├── urls.cpython-312.pyc
│   │   │   ├── validators.cpython-312.pyc
│   │   │   ├── views.cpython-312.pyc
│   │   │   └── viewsets.cpython-312.pyc
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── index.py
│   │   ├── management
│   │   │   └── commands
│   │   │       ├── __pycache__
│   │   │       │   └── createuser.cpython-312.pyc
│   │   │       └── createuser.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   │       ├── 0001_initial.cpython-312.pyc
│   │   │       ├── 0002_alter_product_content.cpython-312.pyc
│   │   │       ├── 0002_product_user.cpython-312.pyc
│   │   │       ├── 0003_alter_product_user.cpython-312.pyc
│   │   │       ├── 0003_product_public.cpython-312.pyc
│   │   │       └── __init__.cpython-312.pyc
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── validators.py
│   │   ├── views.py
│   │   └── viewsets.py
│   └── search
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-312.pyc
│       │   ├── admin.cpython-312.pyc
│       │   ├── apps.cpython-312.pyc
│       │   ├── client.cpython-312.pyc
│       │   ├── models.cpython-312.pyc
│       │   ├── serializers.cpython-312.pyc
│       │   ├── urls.cpython-312.pyc
│       │   └── views.cpython-312.pyc
│       ├── admin.py
│       ├── apps.py
│       ├── client.py
│       ├── migrations
│       │   ├── __init__.py
│       │   └── __pycache__
│       │       └── __init__.cpython-312.pyc
│       ├── models.py
│       ├── serializers.py
│       ├── tests.py
│       ├── urls.py
│       └── views.py
├── js_client
│   ├── client.js
│   └── index.html
├── py_client
│   ├── basic.py
│   ├── create.py
│   ├── creds.json
│   ├── delete.py
│   ├── detail.py
│   ├── jwt.py
│   ├── list.py
│   ├── not_found.py
│   └── update.py
└── requirements.txt
```
