# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@version:
author:MCC
@time: 2019/11/11
@file: wechat_auth.py
@function:
@modify:
"""
from .models import User
from django.contrib.auth.backends import ModelBackend

class WechatOpenidAuth(ModelBackend):
    def get_user(self,open_id):
        try:
            return User.objects.get(pk=open_id)
        except:
            return None
    def authenticate(self,request=None,**kwargs):
        try:
            user = User.objects.filter(open_id=kwargs['open_id']).first()
            if not user:
                user = User()
            return user
        except:
            return None