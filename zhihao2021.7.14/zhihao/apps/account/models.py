#-*-coding:GBK -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# ʹ�ó�������չUser�����User�Ķ����ֶ�
# User��ԭ��11���ֶΣ�id,password,last_login,is_supuser,username,first_name,last_name,email,is_staff,is_active,date_joined
# ��������չ8���ֶΣ�realname,jobrole,qq,weChat,mobile,addr,staff_num,belong
class MyUser(AbstractUser):
    realname = models.CharField('��ʵ����', max_length=20)
    jobrole = models.CharField('Ա����ɫ', max_length=10, blank=True)
    staff_num = models.CharField('Ա�����', max_length=10, blank=True)
    belong = models.IntegerField(verbose_name='����')
    mobile = models.CharField('�ֻ�����', max_length=11, blank=True)
    qq = models.CharField('QQ����', max_length=16, blank=True)
    weChat = models.CharField('΢���˺�', max_length=50, blank=True)
    addr = models.CharField('��ַ��Ϣ', max_length=100, blank=True)
    id_card=models.CharField('���֤����',max_length=50,blank=True)
    # ���÷���ֵ
    def __str__(self):
        return self.username
