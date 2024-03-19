from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import format_html


# Create your models here.
class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    session_key = models.CharField(max_length=100, verbose_name='服务器会话密钥' ,null=True)
    access_key = models.CharField(max_length=100, verbose_name='通用密钥', null=True)
    open_id = models.CharField(max_length=100, verbose_name='openid' ,null=True)
    nickname = models.CharField(max_length=100 , verbose_name='昵称',null=True)
    avatar = models.URLField(verbose_name='头像',null=True)

    def image_data(self):
        if self.avatar:
            return format_html(
                '<img src="{}" width="100px"/>',
                self.avatar,
            )
        else:
            return format_html(
                '<img src="{}" width="100px"/>',
                'https://github.com/mcc321/mcc/blob/master/img/14.jpg?raw=true',
            )

    image_data.short_description = u'头像'

    def update(self,**kwargs):
        arr=[]
        if 'access_key' in kwargs:
            self.access_key = str(kwargs['access_key'])
            arr.append('access_key')
        if 'open_id' in kwargs:
            self.open_id=kwargs['open_id']
            arr.append('open_id')
        if 'session_key' in kwargs:
            self.session_key=kwargs['session_key']
            arr.append('open_id')
            self.password = self.session_key
            arr.append('password')
        if 'nickname' in kwargs:
            self.nickname=kwargs['nickname']
            self.username=self.nickname
            arr.append('nickname')
            arr.append('username')
        if 'avatar' in kwargs:
            self.avatar=kwargs['avatar']
            arr.append('avatar')
        if 'is_active' in kwargs:
            self.is_active = bool(kwargs['is_active'])
            arr.append('is_active')
        if 'is_superuser' in kwargs:
            self.is_superuser = bool(kwargs['is_superuser'])
            arr.append('is_superuser')
        if self.exist():
            self.save(update_fields=arr)
        else:
            self.save()

    def exist(self):
        if User.objects.filter(open_id=self.open_id).first():
            return True
        return False

    class Meta():
        verbose_name = '用户'
        verbose_name_plural = '用户'

    def __str__(self):
        return self.open_id

