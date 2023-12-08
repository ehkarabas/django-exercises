<div align=center>
	<h1>Django CRUD & Auth</h1>
</div>

<div align="center">
      <p>Live API</p>
	<a href="http://djangocrudauth.pythonanywhere.com/products/">
		<img src="https://img.shields.io/badge/API-%23.svg?&style=for-the-badge&logo=www&logoColor=white%22&color=black">
	</a>
	<hr>
</div>

<div align="center">
	<img src="./presentation/django_crud_auth-presentation.gif"/>
	<hr>
</div>

<div align="center">
      <p>You can check presentation as video from below</p>
</div>

[![Go To The Presentation Video](https://i.hizliresim.com/qo9x8bm.png)](https://youtu.be/V6NaquqMNZo)

<hr>

## Description

A responsive product listing platform with an authentication system that prevents unauthorized users from accessing certain sections. The backend is built with Django, and the frontend utilizes Django templates & DTL.

## Backend Goals

Practicing on Django, Django Forms, Django Templates, Django Views, Django Authentication, Django Template Language, CRUD operations with Django functional views, building authentication system with login, register, change password features via Django auth, creating a layout template for general HTML sturcture to include other partial HTML structures like header, footer, messages and app templates in it, limiting access with login_required decorator, customizing default Django forms to add override field cleans & add HTML element attributes like class to fields & adding 'next' field as HiddenInput to redirect after login(POST), redirecting via template that use javascript to display seconds left to redirect, customizing django messages to use tags in compatible with bootstrap, defining static/template/media roots and static/media urls, customizing model and instance appearances on admin panel.

## Technologies

- Django
- Django Forms
- Django Messages
- Django Templates
- Django Authentication
- Django Template Language

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
django-crud-auth(folder)
|
├── README.md
├── account
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   ├── admin.cpython-312.pyc
│   │   ├── apps.cpython-312.pyc
│   │   ├── forms.cpython-312.pyc
│   │   ├── models.cpython-312.pyc
│   │   ├── urls.cpython-312.pyc
│   │   └── views.cpython-312.pyc
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       └── __init__.cpython-312.pyc
│   ├── models.py
│   ├── templates
│   │   └── account
│   │       ├── change_password.html
│   │       ├── login.html
│   │       └── register.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── app1
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   ├── admin.cpython-312.pyc
│   │   ├── apps.cpython-312.pyc
│   │   ├── forms.cpython-312.pyc
│   │   ├── models.cpython-312.pyc
│   │   ├── urls.cpython-312.pyc
│   │   └── views.cpython-312.pyc
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-312.pyc
│   │       └── __init__.cpython-312.pyc
│   ├── models.py
│   ├── static
│   │   ├── css
│   │   │   └── style.css
│   │   ├── images
│   │   └── js
│   │       └── script.js
│   ├── templates
│   │   └── app1
│   │       ├── create.html
│   │       ├── delete_confirm.html
│   │       ├── edit.html
│   │       ├── index.html
│   │       ├── list.html
│   │       ├── product.html
│   │       └── upload.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── django-crud-auth
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   ├── settings.cpython-312.pyc
│   │   ├── urls.cpython-312.pyc
│   │   └── wsgi.cpython-312.pyc
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── presentation
│   └── django_crud_auth-presentation.gif
├── requirements.txt
├── static
│   ├── css
│   │   └── styles.css
│   ├── images
│   │   ├── 1.jpeg
│   │   ├── 2.jpeg
│   │   ├── 3.jpeg
│   │   ├── 4.jpeg
│   │   ├── ehlogo-transparent.png
│   │   ├── ehlogo-transparent.svg
│   │   ├── laptop1.jpg
│   │   ├── laptop2.jpg
│   │   └── no-image.png
│   └── js
├── templates
│   ├── app1
│   │   ├── dizinHakkinda.txt
│   │   └── vscodeDTLkullanimi.txt
│   ├── base.html
│   ├── form_snippet.html
│   ├── partials
│   │   ├── _footer.html
│   │   ├── _header.html
│   │   ├── _messages.html
│   │   └── _noproducts.html
│   └── redirect_message.html
└── uploads
    └── images
        ├── 1.jpeg
        └── 2.jpeg
```
