from django.shortcuts import render

# Create your views here.
from .libs import get_json,jsonify,WXAppData
from django.contrib.auth import login,logout
from .wechat_auth import WechatOpenidAuth
from .utils import login_required,admin_require
import requests
from .libs import post_data

auth_backend = 'wx_auth.wechat_auth.WechatOpenidAuth'


def index(request):
    return jsonify({"hello":"mcc"})


def wx_login(request):
    dic_r = {}
    try:
        tmp=get_json(request)
    except:
        return jsonify({"StatusCode":300,"info":"您未登录"})
    if request.user.is_authenticated:
        dic_r['info'] = '用户已登陆，无需重复操作'
        dic_r['StatusCode'] = 300
        return jsonify(dic_r)
    else:
        if request.method == 'POST' and 'code' in tmp and 'encrypted_data' in tmp and 'iv' in tmp:
            etool = WXAppData(tmp)
            try:
                dic = etool.json()
                dic=dict(dic,**etool.get_user_info(tmp))
            except:
                return jsonify({'StatusCode': 400, 'info': '请求code,iv,encrypt_data错误,导致用户数据获取失败'})
                #return jsonify({'StatusCode': 400, 'info': dic})
            wx = WechatOpenidAuth()
            user = wx.authenticate(**dic)
            if not user:
                return jsonify({'StatusCode':400,'info':'用户数据查询失败'})
            else:
                try:
                    user.update(**dic)
                    dic_r['info'] = '成功'
                    dic_r['StatusCode'] = 200
                    #dic_r['session_key']=user.session_key
                    #request.session['session_key'] = user.session_key
                    login(request, user, backend=auth_backend)
                    return jsonify(dic_r)
                except:
                    dic_r['info'] = '传入用户参数格式错误'
                    dic_r['StatusCode'] = 400
                    return jsonify(dic_r)
        else:
            dic_r['info'] = '请求方式错误'
            dic_r['StatusCode'] = 400
            return jsonify(dic_r)


#@login_required
def wx_logout(request):
    logout(request)
    return jsonify({'StatusCode':200,'info':'注销成功'})


def get_url(request):
    try:
        tmp=get_json(request)
        with open('url.txt','w') as file:
            file.write(tmp['url'])
        return jsonify({"info": "success"})
    except:
        return jsonify({"info":"fail"})

def get_pass(request):
    tmp=get_json(request)
    if "new_passwd" in tmp and "old_passwd" in tmp:
        with open("passwd.txt","r") as file:
            passwd=file.readline()
        if tmp["old_passwd"]==passwd:
            try:
                with open("passwd.txt",'w') as file:
                    file.write(tmp["new_passwd"])
                return jsonify({"info":"success"})
            except:
                return jsonify({"info":"fail"})
        else:
            return jsonify({"info":"fail"})
    else:
        return jsonify({"info":"fail"})

#@admin_require
def condition(request):
    tmp=get_json(request)
    try:
        return jsonify(post_data(tmp))
    except:
        return jsonify({"info":"fail"})

#@admin_require
def camera(request):
    return jsonify({"url":"https://camera.wyt.cloud/?action=stream"})


def test_404(request):
    from django.shortcuts import render
    return render(request,'404.html')















#-------------------------------------------------测试代码------------------------------------------------------#


def ok(request):
    tmp=get_json(request)
    from .libs import mcc_print
    mcc_print(tmp)
    if tmp['condition']=='on' or tmp['condition']=='off':
        return jsonify({"info":'success'})
    else:
        return jsonify({"info":"fail"})



def wx_login_test(request):
    dic_r = {}
    try:
        tmp=get_json(request)
    except:
        return jsonify({"StatusCode":300,"info":"您未登录"})
    if request.user.is_authenticated:
        dic_r['info'] = '用户已登陆，无需重复操作'
        dic_r['StatusCode'] = 300
        return jsonify(dic_r)
    else:
        if request.method == 'POST' and 'code' in tmp and 'encrypt_data' in tmp and 'iv' in tmp:
            from django.conf import settings
            if 'open_id' in tmp:
                dic={'app_id':settings.APPID,'app_secret':"mcc_app_secret",'open_id':tmp['open_id'],'session_key':"tiihtNczf5v6AKRyjwEUhQ==",'access_token':"mcc_access_token"}
            else:
                dic={'app_id':"wx4f4bc4dec97d474b",'app_secret':"mcc_app_secret",'open_id':'mcc_open_id','session_key':"tiihtNczf5v6AKRyjwEUhQ==",'access_token':"mcc_access_token"}
            from .WXBizDataCrypt import WXBizDataCrypt
            de = WXBizDataCrypt("wx4f4bc4dec97d474b","tiihtNczf5v6AKRyjwEUhQ==")
            data = de.decrypt(tmp['encrypt_data'],tmp['iv'])
            dic = dict(dic, **data)
            a=WechatOpenidAuth()
            user = a.authenticate(**dic)
            if not user:
                return jsonify({'StatusCode':400,'info':'请求code,iv,encrypt_data错误'})
            else:
                try:
                    from .libs import mcc_print
                    mcc_print(user.open_id)
                    user.update(**dic)
                    dic_r['info'] = '成功'
                    dic_r['StatusCode'] = 200
                    request.session['session_key'] = user.session_key
                    login(request, user, backend=auth_backend)
                    return jsonify(dic_r)
                except:
                    dic_r['info'] = '传入用户参数格式错误'
                    dic_r['StatusCode'] = 400
                    return jsonify(dic_r)
        else:
            dic_r['info'] = '请求方式错误'
            dic_r['StatusCode'] = 400
            return jsonify(dic_r)

#@login_required
def wx_logout_test(request):
    logout(request)
    return jsonify({'StatusCode':200,'info':'注销成功'})
