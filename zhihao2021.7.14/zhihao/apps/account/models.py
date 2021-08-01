#-*-coding:GBK -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# 使用抽象类扩展User，添加User的额外字段
# User中原有11个字段：id,password,last_login,is_supuser,username,first_name,last_name,email,is_staff,is_active,date_joined
# 这里再扩展8个字段：realname,jobrole,qq,weChat,mobile,addr,staff_num,belong
class MyUser(AbstractUser):
    realname = models.CharField('真实姓名', max_length=20)
    jobrole = models.CharField('员工角色', max_length=10, blank=True)
    staff_num = models.CharField('员工编号', max_length=10, blank=True)
    belong = models.IntegerField(verbose_name='羊场域')
    mobile = models.CharField('手机号码', max_length=11, blank=True)
    qq = models.CharField('QQ号码', max_length=16, blank=True)
    weChat = models.CharField('微信账号', max_length=50, blank=True)
    addr = models.CharField('地址信息', max_length=100, blank=True)
    id_card=models.CharField('身份证号码',max_length=50,blank=True)
    # 设置返回值
    def __str__(self):
        return self.username
