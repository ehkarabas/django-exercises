<div align=center>
	<h1>Blog APP API & Client</h1>
</div>

<div align="center">
      <p>Live API(seperated from frontend for representation)</p>
	<a href="https://blogapitest.pythonanywhere.com/swagger/">
		<img src="https://img.shields.io/badge/API-%23.svg?&style=for-the-badge&logo=www&logoColor=white%22&color=black">
	</a>
	<hr>
</div>

<div align="center">
      <p>Live Blog APP(API <-> Client)</p>
	<a href="https://blog-client-ehkarabas.netlify.app/">
		<img src="https://img.shields.io/badge/APP-%23.svg?&style=for-the-badge&logo=www&logoColor=white%22&color=black">
	</a>
	<hr>
</div>

_Wait a while for the explanatory gif to load... There is an mp4 format of it as well in presentation folder._


<div align="center">
	<img src="./presentation/blog_app_apiclient-presentation.gif"/>
</div>

## Description

A comprehensive API system for a blog application database developed using Django with Django Template Language, and its associated front-end developed using React with MUI & Redux. The system includes an authentication system based on a custom DRF token system with a default user model that has been customized by adding fields. Password reset operations can be performed thanks to the mail server configuration. Unauthorized users can only view the Dashboard. Each user can view the blogs they have created, and can publish drafts to the dashboard or do the reverse. Both the dashboard and the page containing the blogs created by the user have pagination compatible with the backend. Each user can edit or delete the blogs they've created. Comments and likes can be left on blogs. The number of users who have viewed each blog, the number of users who have liked it, and the number of comments blogs have can be displayed. The front-end was handled with React, MUI, Tailwind, Formik-Yup.

## Backend Goals

Practicing on models, field types, admin panel model & instance layout customizations in detail(calculated fields, actions and so on), creating custom user model based on django built-in user model via adding fields on it on models and registering it to admin panel, function based views with request and permission decorators, creating token on user instance creation via signal and deleting token on logging out, drf password reset, mail server configuration on settings for password reset, assigning their values from kwargs dictionary to uidb64 and token to give only two fields to end-user on defining a new password via customized Django's default password reset view, Django Template Language(DTL), creating custom templates, redirecting via success_url class attribute on class based views, extending templates from pre-defined base.html, building static dirs on settings.py & project.urls.py to store css files of templates, redirecting to frontend login via html a(anchor) elements, using templates as views via TemplateView on urls.py, creating a parent model contains common fields and inheriting from it on other models, creating read-only fields with serializermethodfields to calculate & collect data from related models via related_name values on the model(creating a reverse relationship), defining read only fields via read_only_fields on serializers to prevent actions on fields containing model transaction informations, creating a parent view filling a common field and inheriting from it on other views, cancelation of pagination on specific views via pagination_class, filtering get requests according to url querries or url dynamic parameters, overriding the retrieve function in views to create or get an instance of a related model that serves calculations for user transactions, overriding the perform_create & perform_update methods on views to fill a related required field with the user to store author information of blogs/comments in creation process of the blogs/comments, using class methods on classes with get_or_create to toggling likes by the user on the blogs.

## Frontend Goals

Practicing on components, props, tailwind, MUI, theme toggling(via tailwind, MUI and redux persist), redux, redux-toolkit(slices, async thunk, extra reducers, configureStore), axios(custom hook containing instance with authorization configuration), using multiple hooks in another hook via custom hooks, react-router(private router included), .env(to hide API datas), _redirect file in case of refreshing issues on host, taostify, formik to configure and yup to validate forms, React hooks.

## Technologies

Backend:
- Django
- DRF(with token)
- DTL
- Swagger & Redoc
- Grappelli(as admin panel)
- Import-Export & Ckeditor on admin panel
- Corsheaders
- Mail Server(just configuration)

Frontend:
- React(with React Helmet)
- React Router v5
- Material UI(with modals, theme customization in assistance of Tailwind and so on)
- Tailwind(with layer overrides)
- Redux(with persist, slices, async thunk and extra reducers)
- Formik & Yup
- Custom Hooks
- Axios(with instances in a custom hook)
- Toastify

## Installation

To run this app on your local, run commands below on the terminal:

1. Clone main repo on your local.

    ```shell
    $ git clone https://github.com/ehkarabas/django-exercises.git
    ```

2. On this sub-repo, open terminal in ./backend for the backend and:

	2.1. Make sure you've installed python and added python to the system path.


	2.2. Install python environment to this sub-repo.

	    ```shell
	    $ python -m venv env
	    ```

	2.3. Activate python environment.

	    ```shell
	    For powershell:
	    $ .\env\Scripts\activate

	    For git bash:
	    $ source env/Scripts/activate

	    For linux/mac:
	    $ source env/bin/activate
	    ```

	2.4. Install required packages to this sub-repo.

	    ```shell
	    $ python install -r requirements.txt
	    ```

	2.5. Run the server on your browser.

	    ```shell
	    $ python manage.py runserver
	    ```

3. On this sub-repo, open terminal in ./frontend for the frontend and:

	3.1. Install node modules to this sub-repo.

	    ```shell
	    $ yarn install

	    or

	    $ npm install
	    ```

	3.2. Run the app on your browser.

	    ```shell
	    $ yarn start

	    or

	    $ npm start
	    ```

## Resource Structure 

```
blog_api_client(folder)
|
├── backend
│   ├── api
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   │       ├── 0001_initial.cpython-311.pyc
│   │   │       └── __init__.cpython-311.pyc
│   │   ├── models.py
│   │   ├── permissions.py
│   │   ├── __pycache__
│   │   │   ├── admin.cpython-311.pyc
│   │   │   ├── apps.cpython-311.pyc
│   │   │   ├── __init__.cpython-311.pyc
│   │   │   ├── models.cpython-311.pyc
│   │   │   ├── permissions.cpython-311.pyc
│   │   │   ├── serializers.cpython-311.pyc
│   │   │   ├── urls.cpython-311.pyc
│   │   │   └── views.cpython-311.pyc
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── core
│   │   ├── asgi.py
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-311.pyc
│   │   │   ├── urls.cpython-311.pyc
│   │   │   └── wsgi.cpython-311.pyc
│   │   ├── settings
│   │   │   ├── base.py
│   │   │   ├── development.py
│   │   │   ├── __init__.py
│   │   │   ├── production.py
│   │   │   └── __pycache__
│   │   │       ├── base.cpython-311.pyc
│   │   │       ├── development.cpython-311.pyc
│   │   │       └── __init__.cpython-311.pyc
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── db.sqlite3
│   ├── debug.log
│   ├── manage.py
│   ├── requirements.txt
│   ├── static
│   │   └── css
│   │       └── style.css
│   ├── templates
│   │   ├── base.html
│   │   └── users
│   │       └── pw_reset_complete.html
│   └── users
│       ├── admin.py
│       ├── apps.py
│       ├── __init__.py
│       ├── migrations
│       │   ├── 0001_initial.py
│       │   ├── __init__.py
│       │   └── __pycache__
│       │       ├── 0001_initial.cpython-311.pyc
│       │       └── __init__.cpython-311.pyc
│       ├── models.py
│       ├── permissions.py
│       ├── __pycache__
│       │   ├── admin.cpython-311.pyc
│       │   ├── apps.cpython-311.pyc
│       │   ├── __init__.cpython-311.pyc
│       │   ├── models.cpython-311.pyc
│       │   ├── permissions.cpython-311.pyc
│       │   ├── serializers.cpython-311.pyc
│       │   ├── signals.cpython-311.pyc
│       │   ├── urls.cpython-311.pyc
│       │   └── views.cpython-311.pyc
│       ├── serializers.py
│       ├── signals.py
│       ├── tests.py
│       ├── urls.py
│       └── views.py
├── frontend
│   ├── package.json
│   ├── public
│   │   ├── images
│   │   │   ├── blog-app-presentation1.gif
│   │   │   ├── blog-app-presentation2.gif
│   │   │   ├── blog-app-presentation3.gif
│   │   │   └── ehlogo-transparent.png
│   │   ├── index.html
│   │   └── _redirect
│   ├── README.md
│   ├── src
│   │   ├── app
│   │   │   └── store.js
│   │   ├── App.js
│   │   ├── assets
│   │   │   └── FavIcon.js
│   │   ├── components
│   │   │   ├── auth
│   │   │   │   ├── LoginForm.jsx
│   │   │   │   ├── PwResetForm.jsx
│   │   │   │   └── RegisterForm.jsx
│   │   │   ├── blog
│   │   │   │   ├── BlogActions.jsx
│   │   │   │   ├── BlogCard.jsx
│   │   │   │   ├── CommentCard.jsx
│   │   │   │   ├── CommentForm.jsx
│   │   │   │   ├── DeleteModal.jsx
│   │   │   │   ├── DetailsBlogCard.jsx
│   │   │   │   ├── MyBlogsBlogCard.jsx
│   │   │   │   └── UpdateModal.jsx
│   │   │   ├── FavComp.jsx
│   │   │   ├── Footer.jsx
│   │   │   ├── Navbar.jsx
│   │   │   ├── ThemeProviderWrapper.jsx
│   │   │   └── ThemeToggle.jsx
│   │   ├── features
│   │   │   ├── authSlice.jsx
│   │   │   ├── blogSlice.jsx
│   │   │   └── themeSlice.jsx
│   │   ├── helper
│   │   │   └── ToastNotify.js
│   │   ├── hooks
│   │   │   ├── useAuthCall.jsx
│   │   │   ├── useAxios.jsx
│   │   │   └── useBlogCall.jsx
│   │   ├── index.css
│   │   ├── index.js
│   │   ├── pages
│   │   │   ├── About.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   ├── Detail.jsx
│   │   │   ├── Login.jsx
│   │   │   ├── MyBlogs.jsx
│   │   │   ├── NewBlog.jsx
│   │   │   ├── NotFound.jsx
│   │   │   ├── Profile.jsx
│   │   │   ├── PwResetRequest.jsx
│   │   │   └── Register.jsx
│   │   └── rooter
│   │       ├── AppRouter.jsx
│   │       └── PrivateRouter.jsx
│   ├── tailwind.config.js
│   └── yarn.lock
├── presentation
│   ├── blog_app_apiclient-presentation.gif
│   └── blog_app_apiclient-presentation.mp4
└── README.md
```