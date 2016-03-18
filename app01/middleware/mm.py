#!/usr/bin/env python
#-*- coding:utf-8 -*-
from django.shortcuts import HttpResponse,render
class mmm(object):
    def process_response(self,request,response):
        print  HttpResponse('alan response')
        return HttpResponse('alan response')
    def process_request(self,request):
        print HttpResponse('alan request')
    def process_exception(self, request, exception):
        print HttpResponse('alan exception')
    def process_view(self, request, callback, callback_args, callback_kwargs):
        print HttpResponse('alan view')
class xxx(object):
    def process_response(self,request,response):
        print 'xxx response'
        return HttpResponse('xxx response')
    def process_request(self,request):
        print 'xxx request'
    def process_exception(self, request, exception):
        print 'xxx exception'
    def process_view(self, request, callback, callback_args, callback_kwargs):
        print 'xxx view'