tb_checker
==========

A tiny tool to check item price on different host of taobao

Demo
----

There is a demo on my own server: http://checker.yewen.us

Usage under command line
-----

``` bash
usage: checker.py [-h] [-c CORRECT_PRICE] [-r RETRY] [-f] item_id

positional arguments:
  item_id               num_iid to check

optional arguments:
  -h, --help            show this help message and exit
  -c CORRECT_PRICE, --correct_price CORRECT_PRICE
                        correct price should be
  -r RETRY, --retry RETRY
                        retry times
  -f, --full            output all columns
```

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

or use the `run_flask.sh` script

``` bash
$ ./run_flask.sh
```
