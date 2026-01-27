Title: Creating a Django 1.8 Admin Command
Date: 2015-07-10 11:00
Category: Old
Tags: python, django,development
Slug: creating-a-django-1-8-admin-command
Authors: easydevmixin
Summary: How to create admin commands to use with ./manage.py
Status: published

When developing a Django application you will eventually find useful to have some command-line admin commands. There are zillions of reasons you may need them. From generating reports to clear cache data from your app.

In this post we are going to see step by step how to create a Django admin command and how to use it.

Suppose this scenario: your Django app makes use of the cache framework in order to cache the stuff you need and sometimes you may need to clear it in a quick fashion.

Admin commands to the rescue here! Actually it’s quite easy to do it. First of all you need to create this folder and file structure inside one of your existing apps:

    example/
    └── management
    │   ├── commands
    │   │   ├── clearcache.py
    │   │   └── __init__.py
    │   └── __init__.py
    ├── cacheutils.py
    ├── ...
    ...

We have an `example` app and inside it we have a management folder (which is a python package as of the \_\_init\_\_.py file) and one level deeper another python package named `commands`.

It is inside this second package where you place the commands you want to use with the app. In this case we have created a `clearcache.py` file which we will be able to use by issuing the command `python manage.py clearcache`. This is how it looks like when running `./manage.py` without arguments and after placing `example` as an `INSTALLED_APPS`.

    (easydevmixin_ve)vagrant@vagrant-ubuntu-trusty-64:/vagrant/easydevmixin_dev/src$ ./manage.py

    Type 'manage.py help <subcommand>' for help on a specific subcommand.

    Available subcommands:
    ...
    [example]
        clearcache
    ...

Sharp-eyed people will notice a `cacheutils.py`. This is just for using in the example. It just contains dummy functions. The whole code for this module is:

    #!python
    def clear_whole_cache():
        print("Hey, the whole cache is cleared!")


    def clear_partial_cache():
        print("Hey, partial cache is cleared!")

## Developing the command
Now that we have the structure, we need to tell the command what we want it to do. In order for a Django admin command to work, you must create a class named `Command` extending the `BaseCommand` class placed in `django.core.management.base`. At the same time, this class will have to implement, at its minimum, the method `handle(self, \*args, \*\*options)`

Here is how to do it:

    :::python
    from django.core.management.base import BaseCommand, CommandError

    class Command(BaseCommand):
        def handle(self, *args, **options):
            pass


This is a base skeleton for our command. Obviously it won’t do anything, but it won’t crash neither. If the only thing we would like to do is just clear all the cache, we can import our `cacheutils.py` module and just use it inside our `handle` method.

    :::python
    from django.core.management.base import BaseCommand, CommandError
    from example import cacheutils

    class Command(BaseCommand):
        def handle(self, *args, **options):
            try:
                cacheutils.clear_whole_cache()
            except Exception as e:
                raise CommandError("An error has occurred: {}".format(e))


And that would be all… if we just want to clear all our cache! What if we want to clear the cache, but just partially?

## Passing parameters
We can add parameters to our django-admin commands. Currently (as of Django 1.8) the `argparse` library is used. The ability to add commands comes with the addition of the method `add\_arguments(*parser*)`. Suppose, as we said before, we just want to clear the cache partially. The way to do that will depend on the use case. We could add the following:

    :::python
    def add_arguments(self, parser):
        # This is an optional argument
        parser.add_argument(
            '--partial',  # argument flag
            action='store_true',  # action to take, stores true if present
            dest='partial',  # argument name
            default=False,  # it is false by default
            help="Clears the cache partially"  # a help message
        )

You can also add positional (mandatory) arguments. For instance, if you would like to get rid of some specific elements you coud pass along a positional argument the ids of those elements so the command would delete them. Take a look at the **Futher information** below to find mor information on that.

Once we have implemented the `add_arguments(parser)` method we can query the parameters on the `handle(*args, **options)` by asking to `**options`:

    :::python
    if options['partial']:
        cacheutils.clear_partial_cache()
    else:
        cacheutils.clear_whole_cache()

And that’s all! Here's the whole code:

    #!python
    from django.core.management.base import BaseCommand, CommandError
    from example import cacheutils


    class Command(BaseCommand):
        def add_arguments(self, parser):
            # This is an optional argument
            parser.add_argument(
                '--partial',  # argument flag
                action='store_true',  # action to take, stores true if present
                dest='partial',  # argument name
                default=False,  # it is false by default
                help="Clears the cache partially"  # a help message
            )

        def handle(self, *args, **options):
            try:
                if options['partial']:
                    cacheutils.clear_partial_cache()
                else:
                    cacheutils.clear_whole_cache()
            except Exception as e:
                raise CommandError("An error has occurred: {}".format(e))

            self.stdout.write("Command executed successfully")

And here are some actual outputs from the code:

    (easydevmixin_ve)vagrant@vagrant-ubuntu-trusty-64:/vagrant/easydevmixin_dev/src$ ./manage.py clearcache --help
    usage: manage.py clearcache [-h] [--version] [-v {0,1,2,3}]
                                [--settings SETTINGS] [--pythonpath PYTHONPATH]
    ...
      --partial             Clears the cache partially
    (easydevmixin_ve)vagrant@vagrant-ubuntu-trusty-64:/vagrant/easydevmixin_dev/src$ ./manage.py clearcache
    Hey, the whole cache is cleared!
    Command executed successfully
    (easydevmixin_ve)vagrant@vagrant-ubuntu-trusty-64:/vagrant/easydevmixin_dev/src$ ./manage.py clearcache --partial
    Hey, partial cache is cleared!
    Command executed successfully

## Further information
Take a look at the excellent Django documentation on [Writing custom django-admin commands](https://docs.djangoproject.com/en/1.8/howto/custom-management-commands/). I find specially useful the section on [BaseCommand subclasses](https://docs.djangoproject.com/en/1.8/howto/custom-management-commands/#basecommand-subclasses). For the `argparse` library take a look at [16.4. argparse — Parser for command-line options, arguments and sub-commands](https://docs.python.org/3/library/argparse.html#module-argparse)
