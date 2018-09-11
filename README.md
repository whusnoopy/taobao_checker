taobao_checker
==========

A tiny tool to check item price on different host of taobao

taobao_checker is a free software, you can use, modify or distribute it without restriction, visit http://whusnoopy.github.io/taobao_checker/LICENSE.html for more detail

WARNING
-------

As taobao changed their page output, this tool is useless after 2016

Demo
----

~~There is a demo on my own server: http://checker.yewen.us~~

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
$ git clone git@github.com:whusnoopy/taobao_checker.git
$ cd taobao_checker
```

### Prepare a virtual env

``` bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

### Run server

``` bash
$ env/bin/python flask_server.py
```

or use the `run_flask.sh` script

``` bash
$ ./run_flask.sh
```

### Using in your browser

Just open http://localhost:9960 to use this tool

### Stop server

Press `Ctrl` + `C` in terminal if you started server by python, or use `run_flask.sh` script to stop it

``` bash
$ ./run_flask.sh stop
```
