#!/usr/bin/env python
#-*- coding:utf-8 -*-
from django.conf.urls import url
from app01.views import account
urlpatterns = [
    url(r'^login/', account.login),
    url(r'^index/', account.index),
    url(r'^regist/', account.regist),
    # url(r'^test/(\d+)/(\d+)$',views.test),
    url(r'^home/', account.home),
    url(r'^logout/', account.logout),
    url(r'^$', account.index),
    ]