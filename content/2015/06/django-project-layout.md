Title: Django Project Layout
Date: 2015-06-26 11:00
Category: Old
Tags: python, django,development,
Slug: django-project-layout
Authors: easydevmixin
Summary: How do I lay out a new Django project
Status: published

![Generic image of a project layout using PyCharm]({static}../../img/django-project-layout.png)

**Word of warning! This is a long post, so better if you have a cup of coffee/tea/whatever-you-like before start reading :)**
----
In this post I’m going to show you what is the layout I feel most comfortable with when working with Django projects. This requires a bit of manual changes. There are ways to automatise this layout, but I have not done it yet. If someone likes the way I lay Django projects and want to automatise it I will be posting here how to do that.

OK! So how does a Django project looks like just after `django-admin.py startproject :my-super-cool-project`? Lets take a look at it. First I have created a directory named `easydevmixin-django` that will be used as a container for the project.

    (easydevmixin-django)~/projects/django/easydevmixin-django
    easydevmixin@bimbolane $ django-admin.py startproject easydevmixin
    .
    └── easydevmixin
        ├── easydevmixin
        │   ├── __init__.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        └── manage.py

As you can see I have started a new django project (with the cool name of `easydevmixin`) inside my `easydevmixin-django` directory and it has created a first-level directory named `easydevmixin` and a second one with the same name.

For the rest of this post I’m going to consider `easydevmixin-project` as the first-level (or root) directory for our project, so what I’m really considering is that structure:

    easydevmixin-django/   -> First-level or project root
    ├── easydevmixin/      -> Second level, main project code
    │   ├── easydevmixin/  -> Third level, apps and configuration
    │   │   ├── __init__.py
    │   │   ├── settings.py
    │   │   ├── urls.py
    │   │   └── wsgi.py
    │   └── manage.py
    ├── .git/              -> Internal Git files
    ├── .gitignore         -> Git ignore files
    ├── docs/              -> Documentation folder
    ├── requirements/      -> Third-party libraries
    ├── LICENSE            -> License file
    └── README.md          -> README file

## First level
This level is just a container for the whole project. Actually a Django project is not only code. A Django project also contains documentation, references to libraries used, it is managed by a SCM such as Git or Mercurial (you’re using a [SCM](https://en.wikipedia.org/wiki/Version_control), right?), etc... It’s for that kind of elements I use the first level.

## Second level
Here lie the files and directories directly hanging from the first level. I always change the name of this second level to `src` in order to avoid confusion with the third level folder with the same name.

    easydevmixin-django/   -> First-level or project root
    ├── src/               -> Second level, main project code
    │   ├── easydevmixin/  -> Third level, apps and configuration
    │...

### docs
In this directory I usually place the documents that conform the documentation of the project. I believe that the main source of truth for a project is the code itself rather than the documentation because the code is organic in the sense that it evolves, whilst documentation is more like a captured moment in time. This is why, in my humble opinion, documentation tends to become obsolete rather quickly. But, anyway, there are some documents that supports the pass of time better than others. Take as an example notes taken on meetings about agreements on functionalities, the initial intention for the project, if you develop using virtual machines how to spin up one of them with the necessary requirements in order to develop the project, etc...

For me this is the kind of documentation that makes sense to store and I find the `docs/` directory a good place to do it.

### requirements
It is normal to use a bunch of third-party libraries on your project to speed it up. Python has a way to store what are the libraries being used to install them when necessary. Refer to the Creating a requirements file in this blog to know how to do that.

Usually I create separate requirements files depending on the environment where I want to use them. For example, I almost always have a `requirements.txt` containing the main libraries used by the project, and a `requirements-dev.txt` which contains libraries that help me develop the project.

Other requirements files could be `requirements-ci.txt` for use on a continuous integration environment, `requirements-production.txt` for use on a production environment, and so on. In the end, the way that you divide your requirements files depend on how you want to structure your project and the environments you have available.

### LICENSE
This is a simple text file containing the kind of license for your project. It can be the whole license text or a link to a place where the actual license is. Unless the project you are working on is not yours, the type of license depends on you (as if it has any kind of license too!). Here are some references:

- [Copyleft](https://en.wikipedia.org/?title=Copyleft)
- [Copyright](https://en.wikipedia.org/wiki/Copyright)
- [Comparison of free and open-source software licenses](https://en.wikipedia.org/wiki/Comparison_of_free_and_open-source_software_licenses)

### README.md
The main intention for that file is to inform the user about something that it would be good for him to know about the project. For instance, install instructions, commands that can be used in the projects, etc. Take a look at some Github’s project so you can have an idea.

This is usually a simple text file. I’m using a .md extension because I happen to write those files using [Markdown](https://en.wikipedia.org/wiki/Markdown) syntax, which I find very suited for this kind of files and documentation in general.

### .gitignore (or any other ignore file for the SCM you’re using)
This is some of the content I use for files I don’t want to track in a Django project:

    #!git
    # Python compiled classes
    __pycache__/
    *.pyc

    # SQLite databases
    *.sqlite
    *.sqlite3
    *.db

    # Project specific
    src/static/
    src/media/

    # Unit test and coverage
    htmlcov/
    .tox/
    .coverage
    .coverage.*
    .cache
    nosetests.xml
    coverage.xml
    *,cover

    # Translations
    *.mo
    *.pot

    # Mac OS
    .DS_*

    # Editors and IDEs (for PyCharm, SublimeText and Netbeans)
    .idea/
    *.sublime-*
    nbproject/private/
    build/
    nbbuild/
    dist/
    nbdist/
    nbactions.xml
    nb-configuration.xml
    .nb-gradle/

    # Others
    *.~

This is not an exhaustive ignore file list and you should add (or remove) whatever it is suited for your project. Later we will see a couple of files (`local.py` and `secrets.json`) I usually include in this list but deserve an explanation on its own.

## Third level
The third level deal with the different apps we create in a Django app. It also includes the `manage.py` file we use to handle some operations on our project and the folder containing the settings, URLs to listen to and the WSGI (Web Server Gateway Interface) file for the project.

I usually include here too the `media/` and `static/` folders if necessary. I use the `media/` folder mainly to store files uploaded by users (e.g. `FileField` or `ImageField`) and `static/` to keep the static files in the project, but preferably only in development. For production environments it is better to use a dedicated server to store that information (see the excellent post [Using Amazon S3 to Store your Django Site's Static and Media Files](https://www.caktusgroup.com/blog/2014/11/10/Using-Amazon-S3-to-store-your-Django-sites-static-and-media-files/) by Dan Poirier on how to set up Amazon S3 to do that).

## About settings
One of the first things I do when starting a Django project is to change its settings. I like to keep separate settings for different environments. The thing goes more or less like this:

1. Create a directory named `settings` into the directory where the `settings.py` file is.
2. Create a `__init__.py` file in it so it is a package
3. Move the file `settings.py` into `settings` and change its name to `base.py`
4. Create three empty files: `development.py`, `production.py` and `local.py.example`.

The idea behind this is to be able to set up my project depending on the environment I want to make it run. This how the structure will look like:

    src/easydevmixin/settings/
    ├── __init__.py
    ├── base.py
    ├── development.py
    ├── local.py.example
    └── production.py

### `__init__.py`
This file is what makes the `settings` directory a Python package. Being this an important thing it also makes sure that the file `local.py` exists. Later I will explain what the `local.py` file is used for.

    #!python
    # -*- coding: utf-8 -*-

    # This is an __init__.py example file placed into the settings directory
    # It will try to import the module local.py and if not found it will
    # exit with an error message.

    import sys

    try:
        from .local import *
    except ImportError:
        print('local.py file does not exist.')
        print('Go to settings directory and copy local.py.example to local.py')
        sys.exit(-1)

### `base.py`
This is part of the previously known as `settings.py` file. Remember we have moved this file into `settings/` and changed its name to `base.py`.

This file contains settings which are the same no matter the environment. This is an example of a bare `base.py` file.

    #!python
    """
    Django settings for easydevmixin project.

    Generated by 'django-admin startproject' using Django 1.8.2.

    For more information on this file, see
    https://docs.djangoproject.com/en/1.8/topics/settings/

    For the full list of settings and their values, see
    https://docs.djangoproject.com/en/1.8/ref/settings/
    """

    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    import json
    import os
    import sys

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    ADMINS = (
        ('Ramon Maria Gallart', 'rgallart@easydevmixin.com'),
    )

    MANAGERS = ADMINS

    def get_secret(the_secret, debugging):
        """
        As a security measure, all secrets will be kept in a json file named
        secrets.json. This file will not be managed by the version control
        system, but will be available in our documentation repository or
        as an attached file. The main goal of this is that this file should
        not be viewable by no one except us or our team.
        """
        try:
            secrets_file = os.path.join(BASE_DIR, 'settings', 'secrets.json')

            myjson = json.load(open(secrets_file))
            if debugging:
                return myjson['development'][the_secret]
            else:
                return myjson['production'][the_secret]
        except Exception as e:
            print("Something weird happened while retrieving a secret: {}".format(e))
            sys.exit(-1)



    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

    # Application definition

    INSTALLED_APPS = (
        # DJANGO APPS
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # 3RD-PARTY APPS. PLACE HERE EXTERNAL LIBRARIES

        # PROJECT APPS. PLACE HERE THE APPS CREATED

    )

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.middleware.security.SecurityMiddleware',
    )

    ROOT_URLCONF = 'easydevmixin.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'easydevmixin.wsgi.application'


    # Internationalization
    # https://docs.djangoproject.com/en/1.8/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.8/howto/static-files/

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

    MEDIA_ROOT = os.path.join(BASE_DIR, "media")
    MEDIA_URL = "/media/"

    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

    ##########################################################
    # Set up logging directory
    ##########################################################

    # set the directory where you want to write log files
    # this dir will be created if it does not exist
    # Django will die if it cannot be created
    # This is an example of an absolute path:
    # logsdir = os.path.realpath('/home/vagrant/logs')
    # This uses a dir 'logs' in your home directory (/home/vagrant in the example)
    logsdir = os.path.realpath(os.path.join(os.getenv('HOME'), 'logs'))

    try:
        os.stat(logsdir)
    except OSError:
        print("mkdir %s..." % logsdir)
        try:
            os.mkdir(logsdir)
        except OSError as e:
            print("OSError({0}): {1}".format(e.errno, e.strerror))
            print("Could not mkdir %s" % logsdir)
            sys.exit(1)

You can see there is a function here named `get_secret`. This function’s main goal is to get information meant to be kept secret from an external json file, so that secret information is not stored on our SCM.

### `development.py`
When we’re working on a development environment we normally use libraries or settings not intended to be used on production. For instance, one of the main settings in Django is `DEBUG`, which should be set to `True` on development but set to `False` on production. Another one is `ALLOWED_HOSTS` which is a list of hosts our application will listen requests from. It is OK if it’s empty for development, but definitely you want to set it up for production.

Here I will set these settings and a couple of libraries I find useful to have in order to speed up my development process and ease my tests and debugging sessions. These libraries are [`django-debug-toolbar`](https://django-debug-toolbar.readthedocs.io/en/stable/) and [`django-extensions`](https://django-extensions.readthedocs.io/en/latest/) and I encourage you to take a look at them, as they’re pretty amazing.

    #!python
    from .base import *  # We import everything we have previously set up on base.py

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    TEMPLATE_DEBUG = True

    ALLOWED_HOSTS = []


    # Database
    # https://docs.djangoproject.com/en/1.8/ref/settings/#databases
    # Notice here the use of the function get_secret to get information
    # from the secrets.json file which shouldn't be on our VCS
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': get_secret('DB_NAME', DEBUG),
            'USER': get_secret('DB_USER', DEBUG),
            'PASSWORD': get_secret('DB_PASSWORD', DEBUG),
        }
    }

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = get_secret('SECRET_KEY', DEBUG)

    #########################################################
    # Activate django-debug-toolbar if it is installed
    #########################################################
    try:
        import debug_toolbar
        MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
        INSTALLED_APPS += ('debug_toolbar', )
        DEBUG_TOOLBAR_CONFIG = {
            'SHOW_TOOLBAR_CALLBACK': 'easydevmixin.settings.debug_toolbar_stuff.show_toolbar',
        }
    except ImportError:
        pass

    #########################################################
    # Activate django-extensions if exist
    #########################################################
    try:
        import django_extensions
        INSTALLED_APPS += ('django_extensions', )
    except ImportError:
        pass

    # LOGGING. An example of how to set up a basic logging facility
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': "[%(asctime)s] [%(levelname)s] [%(name)s] [%(lineno)s] %(message)s",
                'datefmt': "%d/%m/%Y %H:%M:%S"
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler'
            },
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'simple',
            },
            'example_rotating_file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'verbose',
                'filename': os.path.join(logsdir, 'assets.log'),
                'maxBytes': 1024 * 1024 * 10,
                'backupCount': 10,
            },
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
            'example': {
                'handlers': ['example_rotating_file'],
                'level': 'DEBUG',
            },
        }
    }
Notice the use of the `get_secret` function defined on `base.py`. We are using it to get information about the database and our django’s app secret key.

We are also logging using a `DEBUG` level, something that we will not do on production unless you want to run out of HDD pretty quickly.

### `production.py`
That’s basically the same than production, but with settings tweaked to be production-like.

    #!python
    from .base import *

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = False
    TEMPLATE_DEBUG = False

    # CHANGE THE ALLOWED_HOSTS LIST TO FIT YOUR NEEDS
    ALLOWED_HOSTS = ['www.easydevmixin.com', 'www.easydevmixin.cat']

    # Database
    # https://docs.djangoproject.com/en/1.8/ref/settings/#databases
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': get_secret('DB_NAME', DEBUG),
            'USER': get_secret('DB_USER', DEBUG),
            'PASSWORD': get_secret('DB_PASSWORD', DEBUG),
        }
    }

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = get_secret('SECRET_KEY', DEBUG)

    # LOGGING
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': "[%(asctime)s] [%(levelname)s] [%(name)s] [%(lineno)s] %(message)s",
                'datefmt': "%d/%m/%Y %H:%M:%S"
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler'
            },
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'simple',
            },
            'assets_rotating_file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'verbose',
                'filename': os.path.join(logsdir, 'assets.log'),
                'maxBytes': 1024 * 1024 * 10,
                'backupCount': 10,
            },
            'template_loader_rotating_file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'verbose',
                'filename': os.path.join(logsdir, 'template_loader.log'),
                'maxBytes': 1024 * 1024 * 10,
                'backupCount': 10,
            },
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
            'assets': {
                'handlers': ['assets_rotating_file'],
                'level': 'INFO',
            },
            'template_loader': {
                'handlers': ['template_loader_rotating_file'],
                'level': 'INFO',
            },
        }
    }
The main differences with `production.py` is that `DEBUG` settings have been switched to `False`, we have explicitly stated what our allowed hosts are, there are no development libraries here and the logging level has increased to `INFO`.

You want to place here actual secret keys and config information for any external services you want to use in production (say external API services access, storage, etc...)

### `local.py.example`
This is just a template for `local.py`.

    #!python
    from .development import *

This simply loads everything from `development.py`.

### `local.py`
`manage.py` must load this file in order to run our Django project. This file is not intended to be kept on our SCM, as its main goal is to help developers to set whatever they need in their own environment to develop the application. This could be later needed on the project, so it will be included on `development.py` and `production.py` or it will be discarded, but, anyway, will be something that will not mess up with other developer’s environment.

The way to create it is by copying `local.py.example` to `local.py`.

In order for the file not to be included on our SCM I add a new line under `Project specific`

    src/easydevmixin/settings/local.py

Change the route accordingly so it fits your project.

### `secrets.json` Keep secret your secrets
This is another file that is not meant to be kept under SCM. As before, I add a new line under `Project specific`

    src/easydevmixin/settings/secrets.json

This file holds secrets you don’t want to share publicly (they should not be secrets if you do). For instance, those secrets could be se secret key for your Django app, the database name, username and password, secret keys for external services, etc...

Usually I create a couple of sections into this file: production and development. As a rule of thumb, everything that is not production is development (staging environments, continuous integration environments, test environments, you name it).

This is an example of `secrets.json` file:

    #!json
    {
        "development": {
            "SECRET_KEY": "the-development-django-secret-key",
            "DB_NAME": "the-development-database-name",
            "DB_USER": "the-development-database-username",
            "DB_PASSWORD": "the-development-database-password",
        },
        "production": {
            "SECRET_KEY": "the-production-django-secret-key",
            "DB_NAME": "the-production-database-name",
            "DB_USER": "the-production-database-username",
            "DB_PASSWORD": "the-production-database-password",
        }
    }

## Conclusion
Pheeeew... This has been quite a long (but hopefully useful) post. This is just the way I create Django projects. This doesn’t mean is the best one (neither the worst one) nor that you should stick to it. But it is the one that works best for me and that’s why I’m sharing it with you!

Happy Django layout!
