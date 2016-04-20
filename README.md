# Django Blog Example
Django Example with my first Django Project :)

This repository stores my first Django project using the manual " Django Girls".

The project can be seen at http://amugika.pythonanywhere.com

Start basic steps:

Clone repository.

Install Django last version

```sh
pip install django==1.9
```

# CKEditor Installation Guide & more info

https://github.com/django-ckeditor/django-ckeditor

In this moment configure to use with SQLite DB.

To use MySQL Database change 'settings.py' inside 'youtube_api' directory.

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

In Windows:

```sh
http://stackoverflow.com/questions/8921188/issue-with-virtualenv-cannot-activate
```

Install/Create Connection MySQL in Python:

```sh
(python2.7) $ brew install mysql    # add with libmysqlclient-dev
(python2.7) $ sudo pip install mysql-python
```
Source: http://omaryahir.blogspot.com.es/2014/01/instalar-django-mysql-osx-guia-rapida-5.html

Install PDF Generator (Reportlab):

https://docs.djangoproject.com/en/1.8/howto/outputting-pdf/

```sh
pip install reportlab
```

Install Django CKEditor (Django CKEditor):

https://github.com/django-ckeditor/django-ckeditor

```sh
pip install django-ckeditor
```

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
python manage.py migrate (in Django 1.9 change syncdb with "migrate")

python manage.py makemigrations yourappname

python manage.py migrate

python manage.py createsuperuser (Create user to manage admin panel and content)

```

Execute:
```sh
python manage.py runserver
```

Input 127.0.0.1:8000 in web browser

###Template:
```sh
Template download from http://startbootstrap.com/template-overviews/clean-blog/
```

###Problems & Solutions

Define two foreign keys to the same model (For example: Category)

```sh
http://stackoverflow.com/questions/543377/how-can-i-have-two-foreign-keys-to-the-same-model-in-django
```

Autoescape HTML code:

```sh
{% autoescape off %}{{ variable }}{% endautoescape %} 
```

Encoding error (Add UTF-8 coding in py file)

```sh
http://django.es/blog/anadir-encoding-utf-8-nuestros-archivos-py/
```

Encoding error inside Admin Page:

```sh
http://stackoverflow.com/questions/6560226/django-unicode-error-on-admin-page
```

Count element frecuency inside list

http://stackoverflow.com/questions/2161752/how-to-count-the-frequency-of-the-elements-in-a-list

```sh
>>> a = [1,1,1,1,2,2,2,2,3,3,4,5,5]
>>>
>>> from collections import Counter
>>> c=Counter(a)
>>>
>>> c.values()
[4, 4, 2, 1, 2]
>>>
>>> c.keys()
[1, 2, 3, 4, 5]
```

#Unicode management

```sh
If you are on Python 3, you can skip this section because you’ll always create __str__() rather than __unicode__(). If you’d like compatibility with Python 2, you can decorate your model class with python_2_unicode_compatible(). In python 2 create with __unicode__()
```

https://docs.djangoproject.com/en/1.8/ref/unicode/

#Could not parse the remainder: '[0]' from 'item[0]' Django

http://stackoverflow.com/questions/19895894/could-not-parse-the-remainder-0-from-item0-django

Use item.0 instead of item[0]

```sh
{{ item.0 }}
```

#Django custom admin actions:

https://godjango.com/78-custom-django-admin-actions/


#Permission problems (is not writable user local bin)

http://stackoverflow.com/questions/26647412/homebrew-could-not-symlink-usr-local-bin-is-not-writable

#For Loop Counter inside template:

http://stackoverflow.com/questions/11481499/django-iterate-number-in-for-loop-of-a-template



