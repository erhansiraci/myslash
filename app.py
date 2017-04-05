#!/usr/bin/env python
# encoding: utf-8
import os

from bottle import run, post,request


@post('/checkin')
def hello():
    command = request.forms.get('command')
    text = request.forms.get('text')
    response_text = ""
    if command == '/checkin':
        response_text = "checkin command"
        params = text.split(' ')
    return response_text

if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    run(host='0.0.0.0', port=port)
