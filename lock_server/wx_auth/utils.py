# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@version:
author:MCC
@time: 2019/11/11
@file: utils.py
@function:
@modify:
"""
from .libs import jsonify
from functools import wraps
from django.contrib.auth.decorators import login_required


def auth_require(function):
    """Limit view to auth user only."""
    @wraps(function)
    @login_required
    def auth(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return jsonify({'StatusCode': 300, 'info': 'PermissionDenied'})
        if not request.user.is_active:
            return jsonify({'StatusCode':300,'info':'PermissionDenied'})
        return function(request, *args, **kwargs)
    return auth


def admin_require(function):
    """Limit view to auth user only."""
    @wraps(function)
    @login_required
    def admin(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return jsonify({'StatusCode': 300, 'info': 'PermissionDenied'})
        if not request.user.is_superuser:
            return jsonify({'StatusCode':300,'info':'PermissionDenied'})
        return function(request, *args, **kwargs)
    return admin
