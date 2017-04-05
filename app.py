#!/usr/bin/env python
# encoding: utf-8
import os

from bottle import run, post,request


@post('/inout')
def hello():
    command = request.forms.get('command')
    text = request.forms.get('text')
    response_text = ""
    if command == '/inout':
        response_text = "correct command"
        params = text.split(' ')
        response_text = params
    return response_text

if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    run(host='0.0.0.0', port=port)
