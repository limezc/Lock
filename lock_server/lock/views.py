# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@version:
author:MCC
@time: 2019/11/11
@file: views.py
@function:
@modify:
"""
from django.shortcuts import render

def index(request):
    return render(request,'index.html')