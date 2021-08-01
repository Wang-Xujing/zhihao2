from django.db import models
from django.utils import timezone
from apps.basic.models import BasicInfo
# Create your models here.
class rutInfo(models.Model):
    basic_id=models.IntegerField(verbose_name='羊基本信息id')

    age=models.IntegerField(verbose_name='年龄',blank=True,null=True)##?自动录入，是根据羊基本吗

    breeding_choice=((True,'是'),(False,'否'))
    breeding=models.BooleanField(verbose_name='是否配种',choices=breeding_choice)

    f_staff=models.IntegerField(verbose_name='创建人员',blank=True,null=True)
    f_date=models.DateField(verbose_name='创建时间',default=timezone.now)
    belong = models.IntegerField(verbose_name='羊场域')
    def ele_id(self):
        basic=BasicInfo.objects.filter(id=self.basic_id).values("ele_num").first()
        basic_ele=basic['ele_num']
        return basic_ele    
    class Meta:
        verbose_name='发情信息'
        verbose_name_plural='发情信息'
class SemencollectInfo(models.Model):
    basic_id=models.IntegerField(verbose_name='羊基本信息id')
    E_date=models.DateField(verbose_name='采精日期',blank=True)
    dilution_ratio=models.FloatField(verbose_name='稀释倍数',blank=True,null=True)
    diluent_type=models.CharField(verbose_name='稀释液种类',blank=True,max_length=20)

    disused_choice=((True,'是'),(False,'否'))
    disused=models.BooleanField(verbose_name='是否废弃',choices=disused_choice)
    f_staff=models.IntegerField(verbose_name='创建人员',blank=True,null=True)
    f_date=models.DateField(verbose_name='创建时间',default=timezone.now)
    belong = models.IntegerField(verbose_name='羊场域')
    def ele_id(self):
        basic=BasicInfo.objects.filter(id=self.basic_id).values("ele_num").first()
        basic_ele=basic['ele_num']
        return basic_ele
    class Meta:
        verbose_name='采精信息'
        verbose_name_plural='采精信息'
class breedingInfo(models.Model):
    breeding_date=models.DateField(verbose_name='配种日期',blank=True)
    pre_production_date=models.DateField(verbose_name='预产日期',blank=True)

    breeding_way_choice=((0,'自然交配'),(1,'人工辅助交配'),(2,'人工授精'),(3,'胚胎移植'))
    breeding_way=models.IntegerField(verbose_name='配种方式',choices=breeding_way_choice)

    ewe_id=models.IntegerField(verbose_name='母羊ID',null=True)
    ewe_choice=((0, '湖羊'), (1, '小尾'), (2, '黑山'), (3, '小尾3'), (4, '小尾4'), (5, '小尾5'), (6, '小尾6'))
    ewe_variety=models.IntegerField(verbose_name='母羊品种',blank=True,choices=ewe_choice)##??自动录入
    ram_id=models.IntegerField(verbose_name='公羊ID',null=True)
    ram_choice=((0, '湖羊'), (1, '小尾'), (2, '黑山'), (3, '小尾3'), (4, '小尾4'), (5, '小尾5'), (6, '小尾6'))
    ram_variety=models.IntegerField(verbose_name='公羊品种',blank=True,choices=ram_choice)

    breeding_state_choice=((1,'1'),(2,'2'),(3,'3'))
    breeding_state=models.IntegerField(verbose_name='配种状态',choices=breeding_state_choice)
    staff=models.CharField(verbose_name='操作师',blank=True,max_length=8)
    f_staff=models.IntegerField(verbose_name='创建人员',blank=True,null=True)
    f_date=models.DateField(verbose_name='创建时间',default=timezone.now)
    belong = models.IntegerField(verbose_name='羊场域')
    def ele_id_ewe(self):
        basic=BasicInfo.objects.filter(id=self.ewe_id).values("ele_num").first()
        basic_ele=basic['ele_num']
        return basic_ele
    def ele_id_ram(self):
        basic=BasicInfo.objects.filter(id=self.ram_id).values("ele_num").first()
        basic_ele=basic['ele_num']
        return basic_ele
    class Meta:
        verbose_name='配种信息'
        verbose_name_plural='配种信息'
class pregnantInfo(models.Model):
    check_type=models.CharField(verbose_name='检查类别',max_length=20)
    basic_id=models.IntegerField(verbose_name='羊基本信息id')
    In_pregnancy=models.CharField(verbose_name='孕检信息',blank=True,max_length=40)
    f_staff=models.IntegerField(verbose_name='创建人员',blank=True,null=True)###默认为孕检人员关联表
    f_date=models.DateField(verbose_name='创建人员',default=timezone.now)
    notes=models.TextField(verbose_name='备注',max_length=200,blank=True)
    belong = models.IntegerField(verbose_name='羊场域')
    def ele_id(self):
        basic=BasicInfo.objects.filter(id=self.basic_id).values("ele_num").first()
        basic_ele=basic['ele_num']
        return basic_ele
    class Meta:
        verbose_name='孕检信息'
        verbose_name_plural='孕检信息'
class postnatalInfo(models.Model):
    #添加配种信息id,breeding_id
    breeding_id=models.IntegerField(verbose_name='配种信息id',blank=True,null=True)
    breeding_date=models.DateField(verbose_name='配种日期',blank=True,null=True)##??自动生成
    delivery_date=models.DateField(verbose_name='分娩日期',blank=True,null=True)
    ram_id=models.IntegerField(verbose_name='公羊耳号',blank=True,null=True)
    ewe_id=models.IntegerField(verbose_name='母羊耳号',blank=True,null=True)
    Booroola=models.FloatField(verbose_name='母羊产羔率',blank=True,null=True)###末尾%是否需要

    ewe_health_choice=((True,'正常'),(False,'不正常'))
    ewe_health=models.BooleanField(verbose_name='母羊健康情况',blank=True,choices=ewe_health_choice)

    ewe_condition_choice=((0,'好'),(1,'一般'),(2,'差'))
    ewe_condition=models.IntegerField(verbose_name='母性情况',choices=ewe_condition_choice)
    lamb_ele_num=models.CharField(verbose_name='羊羔耳号',max_length=16,blank=True)

    lamb_state_choice=((0,'健康'),(1,'死亡'),(2,'瘦弱'),(3,'残疾'))
    lamb_state=models.IntegerField(verbose_name='羊羔状态',choices=lamb_state_choice)
    bir_weight=models.FloatField(verbose_name='出生体重',blank=True,null=True)
    live_num=models.IntegerField(verbose_name='产羔数',blank=True,null=True)
    birth_attendants=models.CharField(verbose_name='接生人员',blank=True,max_length=8)
    f_staff=models.IntegerField(verbose_name='创建人员',blank=True,null=True)
    f_date=models.DateField(verbose_name='创建时间',blank=True,default=timezone.now,null=True)
    notes=models.TextField(verbose_name='备注',blank=True,max_length=200)
    belong = models.IntegerField(verbose_name='羊场域')
    def ele_id_ewe(self):
        basic=BasicInfo.objects.filter(id=self.ewe_id).values("ele_num").first()
        basic_ele=basic['ele_num']
        return basic_ele
    def ele_id_ram(self):
        basic=BasicInfo.objects.filter(id=self.ram_id).values("ele_num").first()
        basic_ele=basic['ele_num']
        return basic_ele
    class Meta:
        verbose_name='产后信息'
        verbose_name_plural='产后信息'
class ArtificialfeedingInfo(models.Model):
    ele_id=models.IntegerField(verbose_name='羔羊耳号')
    delivery_date=models.DateField(verbose_name='繁殖日期')
    BW=models.CharField(verbose_name='体重监测',blank=True,max_length=10)
    reason=models.CharField(verbose_name='人工喂养原因',blank=True,max_length=40)
    feeding_material=models.CharField(verbose_name='喂养物',blank=True,max_length=20)
    mcal=models.CharField(verbose_name='食量',blank=True,max_length=20)###食量的单位
    health=models.CharField(verbose_name='健康情况',blank=True,max_length=10)
    help=models.TextField(verbose_name='求助情况',blank=True,max_length=200)
    dose=models.CharField(verbose_name='用量',blank=True,max_length=20)
    feeding_staff=models.CharField(verbose_name='喂养人员',blank=True,max_length=8)
    belong = models.IntegerField(verbose_name='羊场域')
    class Meta:
        verbose_name='人工喂养'
        verbose_name_plural='人工喂养'
class weaningInfo(models.Model):
    basic_id=models.IntegerField(verbose_name='羊基本信息id')
    Delivery_date=models.DateField(verbose_name='繁殖日期')##自动生成

    feeding_way_choice=((0,'哺乳'),(1,'人工'))
    feeding_way=models.IntegerField(verbose_name='喂养方式',choices=feeding_way_choice)
    Bir_weight=models.FloatField(verbose_name='出生体重',blank=True,null=True)
    wea_weight=models.FloatField(verbose_name='出栏体重(断奶体重)',blank=True,null=True)
    ADR=models.CharField(verbose_name='不良反应',blank=True,max_length=40)
    collection=models.CharField(verbose_name='采集量',blank=True,max_length=40)
    feeding_material=models.CharField(verbose_name='喂养食品',blank=True,max_length=40)
    belong = models.IntegerField(verbose_name='羊场域')
    def ele_id(self):
        basic=BasicInfo.objects.filter(id=self.basic_id).values("ele_num").first()
        basic_ele=basic['ele_num']
        return basic_ele
    class Meta:
        verbose_name='断奶信息'
        verbose_name_plural='断奶信息'

