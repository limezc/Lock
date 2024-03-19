import base64
import pyotp
from pyotp import totp
import random
from qrcode import QRCode
import time


# 随机密码生成器
# def GenPassword(length=10, chars=string.ascii_letters.lower()+string.digits):
# return ''.join([choice(chars) for i in range(length)])


# 生成二维码的函数
def get_qrcode(data, *args, **kwargs):
    qr = QRCode(*args,**kwargs)
    qr.add_data(data)
    im = qr.make_image()
    im.show()


# 生成随机google-authenticator密钥的函数
def random_base32(length=16,random=random.SystemRandom(),chars=base64._b32alphabet):
    for i in range(16):
        a=a+random.choice(chars)
    return a


if __name__=='__main__':
    email = "2561908792@qq.com"
    gtoken = pyotp.random_base32()  # google token value
    t = pyotp.TOTP(gtoken)
    data = totp.TOTP(gtoken).provisioning_uri(email, issuer_name="www.wyt.cloud")
    get_qrcode(data)
    key = totp.TOTP.now(t)
    print(key)
    while 1:
        key = totp.TOTP.now(t)
        print(key)
        time.sleep(5)



