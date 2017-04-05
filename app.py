#!/usr/bin/env python
# encoding: utf-8
import os

from bottle import run, post,request


@post('/inout')
def hello():
    command = request.forms.get('command')
    text = request.forms.get('text')
    return 'Hello ' + var + text

if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    run(host='0.0.0.0', port=port)
