Title: How to Install Python 3 on Ubuntu Trusty and CentOS 7
Date: 2015-06-12 11:00
Category: Old
Tags: linux, python, environment
Slug: how-to-install-python-3-on-ubuntu-trusty-and-centos-7
Authors: easydevmixin
Summary: Installing python 3 on two different Linux savors
Status: published

![Python, Ubuntu and CentOS 7 icons]({static}../../img/how-to-install-python-3-on-ubuntu-trusty-and-centos-7.png)

Currently both Ubuntu and CentOS come with some Python 2.7.x flavor of Python. If we want to work with Python 3 we have to install it by ourselves. So let’s start!

## CentOS 7

CentOS is part of the Red Hat family of Linux flavors. Specifically CentOS was born as a port for the RHEL (a.k.a. Red Hat Enterprise Linux). It is mainly known for being an enterprise-ready distribution whose packages have been thoroughly tested for security, stability and reliability.

This also comes with a price. This distribution do not usually have the most cutting-edge packages, but instead most of them are somewhere between 1 and 2 years behind their current stable release.

That being said, the easiest way to install Python 3.4.x on CentOS 7 is by downloading and compiling Python from source. I know it may sound scary, but following these commands step-by-step you will eventually have a running Python 3.4.3 on your system.

```
$ sudo yum groupinstall -y development
$ sudo yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
$ cd /tmp/
$ wget https://www.python.org/ftp/python/3.4.3/Python-3.4.3.tar.xz
$ tar xf Python-3.4.3.tar.xz
$ cd Python-3.4.3
$ ./configure --prefix=/usr/local --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib"
$ make && sudo make altinstall
```

And that’s all! We now have Python 3.4.3 installed on our CentOS 7 system.

## Ubuntu Trusty

If CentOS came from the Red Hat family, Ubuntu derives from Debian. It is currently one of the most successful Linux distributions around (according to [distrowatch.com]), either for business or personal use. It is quite easy to manage and comes itself with a desktop and a server distribution.

It has a predictable release cycle, being every 6 months. Adding to that, every couple of years its XX.04 release is a LTS release (which stands for Long Term Support, and the last one being 14.04, a.k.a. Trusty). What this means is that this release will be receiving security updates for the following five years (at least) versus other releases that only receive updates for 9 months.

Compared to CentOS its packages usually are more up-to-date, so arguably it is easier to develop with top-notch technologies on Ubuntu rather than CentOS.

OK. So we have a couple of ways to install Python 3.4.x on Ubuntu. One is via package manager and the other is by downloading and compiling Python from source, just like we did on CentOS 7.

### Using the package manager

In order to install from the package manager we must first add a repository so that the system will be able to install Python. After doing that it’s just a matter of updating the repository and installing Python.

```
$ sudo add-apt-repository -y ppa:fkrull/deadsnakes
$ sudo apt-get update
$ sudo apt-get -y install python3.4-dev python3.4
```

And that’s all! We have Python 3.4.x installed on our system.

### Compiling Python 3.4.x ourselves

The process is basically the same than the one used with CentOS. The main difference is related to the package manager. CentOS uses yum and Ubuntu uses apt-get. Aside from that and the names of the libraries used, the process is the same.

```
$ sudo apt-get -y install libssl-dev zlib1g-dev libbz2-dev ncurses-dev libsqlite3-dev libreadline-dev tk8.6-dev libgdbm-dev libpcap-dev
$ cd /tmp
$ wget https://www.python.org/ftp/python/3.4.3/Python-3.4.3.tar.xz
$ tar xf Python-3.4.3.tar.xz
$ cd Python-3.4.3
$ ./configure --prefix=/usr/local --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib"
$ make && sudo make altinstall
```

Ant this is it! Python 3.4.3 has been installed on our system!

## Extra bonus!

That’s either for CentOS 7 and Ubuntu. Python 3.4.x comes with pyvenv-3.4, wich is a way to create and work with virtual environments using Python. It comes as a substitute for virtualenv, about which I talked about on ‘[Virtualenv and Pip]({filename}virtualenv-and-pip.md)’.

This is a fairly simple example on how to use it:

```
$ pyvenv-3.4 my34env
$ source my34env/bin/activate
... do whatever you want, for example ...
$ pip install Django==1.8.2
... and when you are done ...
$ deactivate
```

Hope you find it useful and happy Pythoning!
