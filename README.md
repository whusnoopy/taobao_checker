tb_checker
==========

A tiny tool to check item price on different host of taobao

Demo
----

There is a demo on my own server: http://checker.yewen.us

Usage under command line
-----

    usage: checker.py [-h] [-r RETRY] item_id correct_price

    positional arguments:
      item_id               num_iid to check
      correct_price         correct price should be

    optional arguments:
      -h, --help            show this help message and exit
      -r RETRY, --retry RETRY
                            retry times

Usage via web
-------------

### Clone this repo

``` bash
$ git clone git@github.com:whusnoopy/tb_checker.git
$ cd tb_checker
```

### Prepare a virtual env

``` bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirement.txt
```

### Run it

``` bash
$ env/bin/python flask_server.py
```
