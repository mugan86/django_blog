# Django Blog Example
Django Example with my first Django Project :)

This repository stores my first Django project using the manual " Django Girls".

###Tutorial url:

http://tutorial.djangogirls.org/es/index.html

###To use MySQL DB need:

Python 2.7 (Install new virtual environment):

https://plone-spanish-docs.readthedocs.org/es/latest/python/creacion_entornos_virtuales.html

Install Virtual Environment:
```sh
sudo pip install virtualenv
```
Install python 2.7 Virtual Environment:

```sh
virtualenv --python=/usr/bin/python2.7 python2.7
```

Activate:

```sh
source ./python2.7/bin/activate
```

Disactive:

```sh
(python2.7)$ deactivate
```

Install/Create Connection MySQL in Python:

```sh
(python2.7) $ sudo brew install mysql    # add with libmysqlclient-dev
(python2.7) $ sudo pip install mysql-python
```

Source: http://omaryahir.blogspot.com.es/2014/01/instalar-django-mysql-osx-guia-rapida-5.html

###Create database in localhost.

Add Database configuration data in "youtube_api" directory:

```sh
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'django',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
```

Sync model with db and make migration in app 'blog' to create and configure database all tables:

```sh
python manage.py syncdb

python manage.py makemigrations yourappname

python manage.py migrate

```

Execute:
```sh
python manage.py runserver
```

Input 127.0.0.1:8000 in web browser





