# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@version:
author:MCC
@time: 2019/11/11
@file: libs.py
@function:
@modify:
"""
import json
import requests
from django.conf import settings
from django.http import HttpResponse
import logging
from .WXBizDataCrypt import WXBizDataCrypt
from Crypto.Cipher import AES
import base64
import simplejson

class WXAppData:
    def __init__(self,r):
        try:
            self.app_id=settings.APPID
            self.app_secret=settings.APPKEY
            self.iv=r['iv']
            self.encrypted_data = r["encrypted_data"]
            url = 'https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=authorization_code'\
                  % (self.app_id, self.app_secret, r['code'])
            response = requests.get(url)
            r = response.json()
            self.open_id=r['openid']
            self.session_key=r['session_key']
            url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s'\
                  % (self.app_id, self.app_secret)
            response = requests.get(url)
            r = response.json()
            self.access_token = r['access_token']
        except:
            pass

    def get_user_info(self,r):
        pc = WXBizDataCrypt(self.app_id, self.session_key)
        dic=pc.decrypt(r['encrypted_data'], r['iv'])
        dic.update({'nickname':dic.pop("nickName")})
        dic.update({'avatar':dic.pop('avatarUrl')})
        return dic

    def json(self):
        try:
            return{
                'app_id':self.app_id,
                'app_secret':self.app_secret,
                'open_id':self.open_id,
                'session_key':self.session_key,
                'access_token':self.access_token,
                'iv':self.iv,
                'encrypted_data':self.encrypted_data
            }
        except:
            pass


def jsonify(dic):
    return HttpResponse(json.dumps(dic), content_type="application/json")


def mcc_print(info):
    logger = logging.getLogger('django')
    logger.info('=================================================================================================')
    logger.info(info)
    logger.info('=================================================================================================')


def get_json(request):
    return simplejson.loads(request.body)


def pad(text):
    while len(text) % 16 != 0:
        text += '\0'
    return text


def encrypt(data,key,iv):
    iv = pad(iv).encode('utf-8')
    data = pad(data).encode('utf-8')
    key=pad(key).encode('utf-8')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    r = cipher.encrypt(data)
    return str(base64.encodebytes(r), encoding='utf-8')


def decrypt(encrypted_data,key,iv):
    key = pad(key).encode('utf-8')
    iv=pad(iv).encode('utf-8')
    encrypted_data = base64.decodebytes(encrypted_data.encode(encoding='utf-8'))
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = str(cipher.decrypt(encrypted_data), encoding='utf-8').replace('\0', '')
    return decrypted


def post_data(dic):
    try:
        with open('passwd.txt','r') as file:
            passwd=file.readline()
            dic['passwd']=passwd
        r = requests.post(settings.API_URL,data=simplejson.dumps(dic))
        return simplejson.loads(r.text)
    except:
        return {"info":"fail"}


