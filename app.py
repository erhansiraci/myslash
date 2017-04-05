#!/usr/bin/env python
# encoding: utf-8
import os

from bottle import run, post,request


@post('/inout')
def hello():
    var = request.forms.get('command')
    return 'Hello ' + var

if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    run(host='0.0.0.0', port=port)
