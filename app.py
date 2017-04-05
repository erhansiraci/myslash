#!/usr/bin/env python
# encoding: utf-8
import os

from bottle import run, post


@post('/inout')
def hello():
    return 'Hello INOUT!'


if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    run(host='0.0.0.0', port=port)
