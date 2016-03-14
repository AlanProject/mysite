#!/usr/bin/env python
#-*- coding:utf-8 -*-

from wsgiref.simple_server import make_server

def runserver(eviron,start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>Hello, web!</h1>'

if __name__ =='__main__':
    httpd = make_server('',8080,runserver)
    httpd.serve_forever()