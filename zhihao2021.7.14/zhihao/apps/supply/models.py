from django.db import models
from django.utils import timezone

# Create your models here.



# 疫苗厂商
class v_suppliersInfo(models.Model):
    belong = models.IntegerField(verbose_name="羊场域")
    supplier_name = models.CharField(verbose_name="厂商名称", max_length=20, blank=True)
    sale_type = models.TextField(verbose_name="疫苗出售类型", max_length=50,blank=True)
    sup_linkman = models.CharField(verbose_name="联系人", max_length=5,blank=True)
    sup_contact = models.CharField(verbose_name="联系人电话", max_length=11,blank=True)
    contact = models.CharField(verbose_name="厂商电话", max_length=11, blank=True,null=True)
    mail = models.CharField(verbose_name="邮箱", max_length=25, blank=True,null=True)
    address = models.CharField(verbose_name="地址", max_length=40)
    f_date = models.DateField(verbose_name="创建时间", default=timezone.now)
    f_staff = models.CharField(verbose_name='创建人员', blank=True, null=True, max_length=20)
    operation = models.TextField(verbose_name="操作", max_length=20,blank=True,null=True)



    class Meta:
        ordering = ('-f_date',)
        verbose_name = '疫苗厂商信息'
        verbose_name_plural = '疫苗厂商信息'




#饲料厂商
class f_suppliersInfo(models.Model):

    belong = models.IntegerField(verbose_name="羊场域")
    supplier_name = models.CharField(verbose_name="厂商名称", max_length=20, unique=True)
    sale_type = models.TextField(verbose_name="饲料出售类型", max_length=50)
    sup_linkman = models.CharField(verbose_name="联系人", max_length=5)
    sup_contact = models.CharField(verbose_name="联系人电话", max_length=11)
    contact = models.CharField(verbose_name="厂商电话", max_length=11, blank=True)
    mail = models.CharField(verbose_name="邮箱", max_length=25, blank=True)
    address = models.CharField(verbose_name="地址", max_length=40,blank=True,null=True)
    f_date = models.DateField(verbose_name="创建时间", default=timezone.now)
    f_staff = models.CharField(verbose_name='创建人员', blank=True, null=True, max_length=20)
    operation = models.TextField(verbose_name="操作", max_length=20,blank=True,null=True)

    class Meta:
        ordering = ('-f_date',)
        verbose_name = '饲料厂商信息'
        verbose_name_plural = '饲料厂商信息'

#保险
class insuranceinfo(models.Model):

    belong = models.IntegerField(verbose_name="羊场域")

    in_name = models.CharField(verbose_name="保险公司", max_length=20, unique=True)
    contact = models.CharField(verbose_name="公司电话", max_length=11)
    mail = models.CharField(verbose_name="公司邮箱", max_length=25, blank=True)
    handler = models.CharField(verbose_name="保险理赔员", max_length=5)
    link = models.CharField(verbose_name="保险员电话", max_length=11)
    f_date = models.DateField(verbose_name="创建时间", default=timezone.now)
    f_staff = models.CharField(verbose_name='创建人员', blank=True, null=True, max_length=20)

    class Meta:
        ordering = ('-f_date',)
        verbose_name = '保险公司信息'
        verbose_name_plural = '保险公司信息'

class commodityInfo(models.Model):

    type_choices = ((0, '疫苗'), (1, '药品'))
    type = models.IntegerField(verbose_name="类别", choices=type_choices)

    cname = models.CharField(verbose_name="名称", max_length=20)

    explain = models.TextField(verbose_name="说明", max_length=50, blank=True,null=True)
    f_staff = models.CharField(verbose_name='创建人员', blank=True, null=True, max_length=20)
    belong = models.IntegerField(verbose_name="羊场域")
    class Meta:
        verbose_name = '疫苗药品信息'
        verbose_name_plural = '疫苗药品信息'