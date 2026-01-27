Title: Virtualenv and Pip
Date: 2015-06-07 11:00
Category: Old
Tags: python, environment
Slug: virtualenv-and-pip
Authors: easydevmixin
Summary: Installing and using virtualenv and pip
Status: published


As the first post in my blog (well, second one really) I want to show you why I find that couple of tools so important to me. So, what are virtualenv and pip?

### Target audience
This post is mainly for developers using Linux. For installing on Mac OSX take a look at this excellent post from [Marina Mele's blog](http://www.marinamele.com/2014/05/install-python-virtualenv-virtualenvwrapper-mavericks.html).

## TL; DR;
Pip installs Python packages and Virtualenv isolates different Python environments. These are the commands shown in this post.

**Install pip:** `curl https://bootstrap.pypa.io/get-pip.py > get-pip.py && sudo python get-pip.py`
**Install Python package system-wide:** `sudo pip install Django==1.8.2`
**Install Virtualenv system-wide:** `sudo pip install virtualenv`
**Create virtual environment ‘test’:** `virtualenv test`
**Deactivate virtual environment (any):** `deactivate`
**Create virtual environment with specific Python version:** `virtualenv --python=$(which python3.4) test_python3.4`
**Check Python packages installed:** `pip freeze --local`

## [Pip](https://pip.pypa.io/en/latest/)
Pip is a tool used to install Python packages. Odds are that if you have Python installed (>=2.7.9 for Python2 or >=3.4 for Python3) you already have pip installed on your system.

### Installing pip
What works better for me is downloading the installer:

`vagrant@precise64:/tmp$ curl https://bootstrap.pypa.io/get-pip.py > get-pip.py`

and then running:

`vagrant@precise64:/tmp$ sudo python get-pip.py`

Doing this we will ensure ourselves that we have pip installed and available on the whole system.

### Using pip
Once pip is on our system, installing Python packages is quite straightforward. For example, if we want to install Django we just execute:

`vagrant@precise64:/tmp$ sudo pip install Django==1.8.2`

And Django 1.8.2 will get installed on your system.

## [Virtualenv](https://virtualenv.pypa.io/en/latest/index.html)
What if you are working on a couple of different Django projects? One using Django 1.7 and the other Django 1.8.2? We’ve seen previously that installing Django using pip like this:

`vagrant@precise64:/tmp$ sudo pip install Django==1.8.2`

would install Django 1.8.2 system-wide. So, what do we have to do when we want to work with the project using Django 1.7? Do we uninstall Django 1.8.2 and then install Django 1.7? That could probably work, but it is a hassle to do that everytime you want to switch projects and quite prone to errors.

Give your welcome to Virtualenv! This piece of software allows you to create python-isolated environments in such a way that it allows you to install different versions of third-party libraries without messing with the ones you could have installed system-wide or on another virtual environment.

This is important because different projects probably will need different libraries and, what is more, different versions of those libraries. We’ve seen Django as an example.

### Installing virtualenv
So, the first step is to install Virtualenv. For this we will use our previously installed pip:

`vagrant@precise64:/tmp$ sudo pip install virtualenv`

This will install virtualenv system-wide.

### Using virtualenv
To create a new virtual environment we just have to issue the following command:

`virtualenv ENV`

Where `ENV` is the name you want to give to your environment. For example (I’m using here `/tmp` to create the virtual environment, but you can use whatever directory you have write permissions on. Mostly that will be something like `/home/youruser/projects/yourproject/yourvirtualenvironment`):

```
vagrant@precise64:/tmp$ virtualenv test
New python executable in test/bin/python
Installing setuptools, pip, wheel...done.

vagrant@precise64:/tmp$ ll
total 4308
drwxrwxrwt  3 root     root        4096 Jun  3 11:48 ./
drwxr-xr-x 24 root     root        4096 Jun  3 10:36 ../
-rw-rw-r--  1 vagrant  vagrant  1421845 Jun  3 11:32 get-pip.py
drwxrwxr-x  6 vagrant  vagrant     4096 Jun  3 11:48 test/
```

When we want to make use of the virtual environment we must first activate it:

```
vagrant@precise64:/tmp$ source test/bin/activate
(test)vagrant@precise64:/tmp$
```

Pay attention to `(test)`. That means we have our environment active. Now we can use pip to install whatever Python package we want and it will reside only in our virtual environment.

```
(test)vagrant@precise64:/tmp$ pip install Django==1.7.6
/tmp/test/local/lib/python2.7/site-packages/pip/_vendor/requests/packages/urllib3/util/ssl_.py:90: InsecurePlatformWarning: A true SSLContext object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning.
  InsecurePlatformWarning
Collecting Django==1.7.6
/tmp/test/local/lib/python2.7/site-packages/pip/_vendor/requests/packages/urllib3/util/ssl_.py:90: InsecurePlatformWarning: A true SSLContext object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning.
  InsecurePlatformWarning
  Downloading Django-1.7.6-py2.py3-none-any.whl (7.4MB)
    100% |################################| 7.4MB 73kB/s
Installing collected packages: Django
Successfully installed Django-1.7.6

(test)vagrant@precise64:/tmp$
```

So now we have installed Django 1.7.6 just into our `test` virtual environment. We can check this issuing the command `pip freeze --local` that will report to us the packages installed:

```
(test)vagrant@precise64:/tmp$ pip freeze --local
Django==1.7.6
wheel==0.24.0

(test)vagrant@precise64:/tmp$
```

If we deactivate our virtual environment and run that last command for the whole system we will find the results are different:

```
(test)vagrant@precise64:/tmp$ deactivate
vagrant@precise64:/tmp$ pip freeze --local
apt-xapian-index==0.44
chardet==2.0.1
command-not-found==0.2.44
Django==1.8.2
GnuPGInterface==0.3.2
language-selector==0.1
python-apt===0.8.3ubuntu7
python-debian===0.1.21ubuntu1
ufw==0.31.1.post1
virtualenv==13.0.3
wheel==0.24.0

vagrant@precise64:/tmp$
```

You can tell virtualenv which Python version you want to use. Assuming you have Python 3.4 installed you could issue this command to get a virtual environment using Python 3.4:

```
vagrant@precise64:/tmp$ virtualenv --python=`which python3.4` test_python3.4
Running virtualenv with interpreter /usr/bin/python3.4
Using base prefix '/usr'
New python executable in test_python3.4/bin/python3.4
Also creating executable in test_python3.4/bin/python
Installing setuptools, pip, wheel...done.
vagrant@precise64:/tmp$ . test_python3.4/bin/activate
(test_python3.4)vagrant@precise64:/tmp$ python --version
Python 3.4.3

vagrant@precise64:/tmp$
```

## There is more
Both Pip and Virtualenv have lots of options more. I just want to keep my posts as simple as possible to get you started, but you can find a lot more information on the documentation sites for the projects ([pip](https://pip.pypa.io/en/latest/) and [virtualenv](https://virtualenv.pypa.io/en/latest/index.html)).
