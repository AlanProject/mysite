#!/usr/bin/env python
#-*- coding:utf-8 -*-
from django.conf.urls import url
import views
urlpatterns = [
    url(r'^login/', views.login),
    url(r'^index/', views.index),
    url(r'^regist/', views.regist),
    # url(r'^test/(\d+)/(\d+)$',views.test),
    url(r'^$',views.index),
    ]