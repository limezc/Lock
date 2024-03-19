# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@version:
author:MCC
@time: 2019/11/11
@file: urls.py
@function:
@modify:
"""

from django.conf.urls import url
from . import views

app_name = 'wx_auth'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^wx_login$', views.wx_login, name='wx_login'),
    url(r'^wx_logout$', views.wx_logout, name='wx_logout'),
    url(r'^get_url$', views.get_url, name='get_url'),
    url(r'^wx_logout_test$', views.wx_logout_test, name='wx_logout_test'),
    url(r'^wx_login_test$', views.wx_login_test, name='wx_login_test'),
    url(r'^condition$', views.condition, name='condition'),
    url(r'^ok$', views.ok, name='ok'),
    url(r'^test_404$', views.test_404, name='test_404'),
    url(r'^camera$', views.camera, name='camera'),
    url(r'^get_pass$', views.get_pass, name='get_pass'),
]
