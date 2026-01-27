Title: Creating a Requirements File
Date: 2015-06-19 11:00
Category: Old
Tags: python,development,
Slug: creating-a-requirements-file
Authors: easydevmixin
Summary: How to create a requirements file for Python development projects
Status: published

When working with a Python project it is important to keep track on the third-party libraries used and what version of these libraries have been used. We all know what happens when we are developing with some libraries but then we get our project to production and everything is messed up. Usually the reason is because we have not installed all of the required libraries for our project or we have installed them all, but their versions differ from the ones we used to develop.

An easy way to keep track of the libraries we use on our Python project is by using what are called requirements files. These are just plain text files composed of names of libraries and their versions.

When developing, usually the thing goes like this (oversimplified):
1. You kick-off your project
2. Code
3. You install some libraries to solve some problems
4. Steps 2 and three keep looping until the end of the project
5. Project ends

Ideally, those requirements files should be updated every time a library gets installed if it will be needed on the different environments (development/staging/production… you name them). Personally I like to keep requirements files in their own directory (I usually call it `tools` or `requirements`) just under the root of the project. For example:

    - project_root/
     |-- src/
     |---- directories and source files of the project
     |-- tools/
     |---- requirements.txt
     |---- requirements-dev.txt
     |---- requirements-prod.txt
     |---- ...

In this example I have placed three requirements files. `requirements.txt` is intended for use on every environment. The `requirements-dev.txt` is only to be used on development environments. For example, it could have some debug helping libraries not suited for a production environment. `requirements-prod.txt` should only have libraries related to a production environment. Maybe a WSGI library like Gunicorn, for example.

And how do we create those files? Guess what? The easiest way to do that is using pip! Suppose you have looped through steps 2 and 3 stated before. How do we get a list of the already installed libraries? Easy! Use pip!

    (project_ve)vagrant@easydev:/vagrant/project_root$ ls -l
    total 4
    -rw-r--r-- 1 vagrant vagrant  60 May 30 09:51 README.md
    drwxr-xr-x 1 vagrant vagrant 476 May 30 10:39 src
    drwxr-xr-x 1 vagrant vagrant 238 Jun 16 15:31 tools
    (project_ve)vagrant@easydev:/vagrant/project_root$ pip freeze --local
    Django==1.6.11
    MySQL-python==1.2.5
    Pillow==2.4.0
    South==0.8.4
    (project_ve)vagrant@easydev:/vagrant/project_dev$

We’ve seen the libraries installed. Lets place them on our requirements file:

    (project_ve)vagrant@easydev:/vagrant/project_root$ pip freeze --local > tools/requirements.txt
    (project_ve)vagrant@easydev:/vagrant/project_root$ cat tools/requirements.txt
    Django==1.6.11
    MySQL-python==1.2.5
    Pillow==2.4.0
    South==0.8.4
    (project_ve)vagrant@easydev:/vagrant/project_root$

From that point on it is a matter of keeping those files updated with whatever new libraries you add to the project or even if the library version used changes.

## Installing from a requirements file

We’ve seen how to get the libraries used, but how do we leverage these files when creating a new environment? The answer is quite easy. Use [pip]({filename}./virtualenv-and-pip.md)! :) Suppose one of your colleagues has span up a new dev machine for her and has to install the libraries. Once she has downloaded the project from the Git repo (you are using Git, Mercurial or some kind of code repo, don’t you?) and activated her virtual environment, she would just go to the project root directory and:

    (project_ve)vagrant@colleague:/vagrant/project_root$ pip install -r tools/requirements.txt
    ...
    lots of downloads and installs
    ...
    (project_ve)vagrant@colleague:/vagrant/project_root$

You can find more detailed information on requirements files and how to use them on [https://pip.pypa.io/en/stable/user\_guide.html#requirements-files](https://pip.pypa.io/en/stable/user_guide.html#requirements-files).

So that’s all! Hope you liked it and find it useful!
