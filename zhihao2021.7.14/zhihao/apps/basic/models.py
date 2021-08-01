from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from apps.colony.models import HouseInfo
from apps.valid import valid_null
from apps.valid import valid_boolean
# Create your models here.
class BasicInfo(models.Model):
    # id = models.AutoField(primary_key=True)       # 自动，自增长
    ele_num = models.CharField(verbose_name="电子耳号", max_length=16, unique=True)
    pre_num = models.CharField(verbose_name="防疫耳号", max_length=16, unique=True, blank=True)

    purpose_choices = ((0, '种羊(待分类)'), (1, '育肥'),(2,'哺乳羔羊'),(5,'繁殖公羊'),(6,'繁殖母羊'),(8,'育成羊'))
    purpose = models.IntegerField(verbose_name='用途', choices=purpose_choices,blank=True,null=True)

    variety_choices = ((0, '湖羊'), (1, '小尾寒羊'), (2, '无角道赛特'), (3, '道寒杂交F1'), (4, '白杜泊'), (5, '白萨福克'), (6, '杜湖杂交'),(7,'萨湖杂交'),(8,'杜寒杂交'),(9,'萨寒杂交'),(10,'道湖'))
    variety = models.IntegerField(verbose_name='品种', choices=variety_choices, blank=True,null=True)

    sex_choices = ((1, '母'), (0, '公'))
    sex = models.IntegerField(verbose_name='性别', choices=sex_choices,blank=True,null=True)

    manu_info_id = models.IntegerField(verbose_name='源产地id', blank=True,null=True)
    manu_info_name=models.CharField(verbose_name='产地名',max_length=50,blank=True,null=True)
    state_choices = ((0, '死亡'), (1, '正常'), (2, '销售'))
    state = models.IntegerField(verbose_name='状态', choices=state_choices,blank=True,null=True)
    ##
    birth = models.DateField(verbose_name='出生日期', default=timezone.now)
    bir_weight = models.FloatField(verbose_name='出生重(kg)', blank=True,null=True)
    wea_weight = models.FloatField(verbose_name='断奶重(kg)', blank=True,null=True)

    house_id = models.IntegerField(verbose_name='圈舍号', blank=True,null=True)##关联id
    hurdle_id=models.IntegerField(verbose_name='圈栏号',blank=True,null=True)##关联id
    house_name=models.CharField(verbose_name='圈栏名称',blank=True,max_length=30,null=True)
    hurdle_name=models.CharField(verbose_name='圈栏名称',blank=True,max_length=30,null=True)

    mon_age = models.FloatField(verbose_name='月龄', blank=True,null=True)
    ##新添加字段
    color_choice = ((0, '白'), (1, '黑'), (2, '咖'), (3, '混合色'))
    color = models.IntegerField(verbose_name='毛色', blank=True,null=True, choices=color_choice)

    rank_choice = ((0, '特级'), (1, '一级'), (2, '二级'),(3,'三级'),(9,'未评级'))
    rank = models.IntegerField(verbose_name='外貌等级', blank=True,null=True, choices=rank_choice)

    ##
    father_id=models.IntegerField(verbose_name='父ID',blank=True,null=True)##关联id
    mother_id=models.IntegerField(verbose_name='母ID',blank=True,null=True)##关联id

    f_ele_num = models.CharField(verbose_name="父电子耳号", max_length=16,blank=True,null=True)
    f_pre_num = models.CharField(verbose_name="父防疫耳号", max_length=16,blank=True,null=True)
    m_ele_num = models.CharField(verbose_name="母电子耳号", max_length=16,blank=True,null=True)
    m_pre_num = models.CharField(verbose_name="母防疫耳号", max_length=16,blank=True,null=True)

    f_staff = models.CharField(verbose_name="创建人员", blank=True,null=True,max_length=20)##用户表
    f_date = models.DateField(verbose_name="创建时间", default=timezone.now, blank=True,null=True)

    img_positive = models.ImageField(verbose_name="正面照片", upload_to='images/pos/%Y/%m/%d', blank=True)
    img_left = models.ImageField(verbose_name="左侧照片", upload_to='images/left/%Y/%m/%d', blank=True)
    img_right = models.ImageField(verbose_name="右侧照片", upload_to='images/right/%Y/%m/%d', blank=True)
    note = models.TextField(verbose_name="备注信息", max_length=300,blank=True,null=True)
    belong = models.IntegerField(verbose_name='羊场域')
    def xipu(self):
        return '查看'
    class Meta:
        ordering = ('-f_date',)
        verbose_name = '羊只基本信息'
        verbose_name_plural = "羊只基本信息"

    def __str__(self):
        return self.ele_num
class manuInfo(models.Model):
    manu_name = models.CharField(verbose_name='厂家名称', max_length=40, unique=True)

    scale_choice = ((0, '国家级'), (1, '省级'), (2, '市级'), (3, '县级'))
    scale = models.IntegerField(verbose_name='养殖场规模', choices=scale_choice)

    type_choice = ((0, '扩繁场'), (1, '育肥场'))
    type = models.IntegerField(verbose_name='养殖场类型', choices=type_choice)

    BP_license_num = models.CharField(verbose_name='种畜禽经营许可证编号', max_length=30, blank=True)
    AP_certificate_num = models.CharField(verbose_name='动物防疫合格证编号', max_length=30, blank=True)
    BL_num = models.CharField(verbose_name='营业执照编号', max_length=30, blank=True)

    legal = models.CharField(verbose_name='法人', max_length=10, blank=True)
    address = models.CharField(verbose_name='地址', max_length=50, blank=True)
    contact = models.CharField(verbose_name='联系方式', max_length=15, blank=True)
    province = models.CharField(verbose_name='所属省', max_length=8, blank=True)
    city = models.CharField(verbose_name='市/县', max_length=8, blank=True)
    belong = models.IntegerField(verbose_name='羊场域')
    class Meta:
        verbose_name='羊只产地信息'
        verbose_name_plural='羊只产地信息'

class elechangeInfo(models.Model):
    basic_id = models.IntegerField(verbose_name='羊只基本信息id')

    new_num = models.CharField(verbose_name="新耳号", max_length=16, unique=True)
    old_num = models.CharField(verbose_name="旧耳号", max_length=16, unique=True)
    retime = models.DateField(verbose_name='更换时间', blank=True)
    reason = models.TextField(verbose_name='更换原因',max_length=50)
    ##!
    sheep_type =models.CharField(verbose_name='羊只类型',max_length=10,blank=True)###是否自动生成
    house_num =models.IntegerField(verbose_name='圈舍号',blank=True,null=True)
    staff =models.CharField(verbose_name='更换人员',blank=True,max_length=8)
    f_date = models.DateField(verbose_name='创建时间', default=timezone.now)
    belong = models.IntegerField(verbose_name='羊场域')
    class Meta:

        verbose_name='耳号更换信息'
        verbose_name_plural='耳号更换信息'

class BreederconditionInfo(models.Model):
    date = models.DateField(verbose_name='测量日期')
    basic_id = models.IntegerField(verbose_name='羊基本信息id')

    age = models.IntegerField(verbose_name='年龄', blank=True,null=True)  ##!
    ##!
    ###1.5号新加字段
    mon_age_choice=((0,'2月龄'),(1,'6月龄'),(2,'12月龄'),(3,'24月龄'),)
    mon_age=models.IntegerField(verbose_name='月龄',choices=mon_age_choice,blank=True,null=True)
    color_choice = ((0, '白'), (1, '黑'), (2, '咖'), (3, '混合色'))
    color = models.IntegerField(verbose_name='毛色', choices=color_choice,validators=[valid_null],blank=True,null=True)

    rank_choice = ((0, '特级'), (1, '一级'), (2, '二级'),(3,'三级'),(9,'未评级'))
    rank=models.IntegerField(verbose_name='外貌等级',choices=rank_choice,blank=True,null=True)
    ###
    high = models.FloatField(verbose_name='体高', blank=True,null=True)
    weight = models.FloatField(verbose_name='体重', blank=True,null=True)
    Llong = models.FloatField(verbose_name='斜体长', blank=True,null=True)
    bust = models.FloatField(verbose_name='胸围', blank=True,null=True)

    testis_shape_choice = ((True, '正常'), (False, '非正常'))
    testis_shape = models.BooleanField(verbose_name='睾丸形状', choices=testis_shape_choice,blank=True,null=True)

    t_staff = models.CharField(verbose_name='测量人员', max_length=8, blank=True)  ###是否为工号
    AE = models.TextField(verbose_name='外貌评定', blank=True,max_length=200)  ##需要多长的外贸评定
    performance_traits = models.CharField(verbose_name='生产性能', blank=True,max_length=40)  ##生产性能怎么表示
    with_births = models.IntegerField(verbose_name='同胎数', blank=True,null=True)

    wea_weight = models.FloatField(verbose_name='断奶重', blank=True,null=True)
    June_heavy = models.FloatField(verbose_name='六月重', blank=True,null=True)
    health = models.CharField(verbose_name='健康情况', blank=True, max_length=40)  ##健康情况所需要的长度

    f_date = models.DateField(verbose_name='创建时间', default=timezone.now)
    f_staff=models.CharField(verbose_name='创建人员',blank=True,null=True,max_length=20)  ###同上

    notes = models.TextField(verbose_name='备注', blank=True,max_length=200)
    belong = models.IntegerField(verbose_name='羊场域')
    def ele_id(self):
        basic=BasicInfo.objects.filter(id=self.basic_id).values("ele_num")
        basic_ele=basic[0]['ele_num']
        return basic_ele
    class Meta:
        verbose_name_plural='种羊体况'
        verbose_name = '种羊体况'

class cutInfo(models.Model):
    house_id = models.IntegerField(verbose_name='圈舍号')  ###关联表的id，是否为圈舍号？
    ele_quantity =models.IntegerField(verbose_name='羊只数量',blank=True,null=True)  ######?是电子耳号还是羊只数量

    variety_choices = ((0, '湖羊'), (1, '小尾寒羊'), (2, '无角道赛特'), (3, '道寒杂交F1'), (4, '白杜泊'), (5, '白萨福克'), (6, '杜湖杂交'),(7,'萨湖杂交'),(8,'杜寒杂交'),(9,'萨寒杂交'),(10,'道湖'))
    variety = models.IntegerField(verbose_name='品种', choices=variety_choices, null=True)

    cut_time_choice = ((3, '3月'), (6, '6月'), (9, '9月'))
    cut_time = models.IntegerField(verbose_name='剪毛时间',null=True, choices=cut_time_choice)

    rank_choice = ((0, '细毛'), (1, '粗毛'), (2, '绒毛'),(3,'细毛-同质'),(4,'粗毛同质'))  # ？？？细毛同质，每种下分同异质？
    rank = models.IntegerField(verbose_name='羊毛类型', null=True,choices=rank_choice)

    color_choice = ((0, '白'), (1, '黑'), (2, '咖'), (3, '混合色'))
    color = models.IntegerField(verbose_name='毛色', null=True, default=0,choices=color_choice)

    weight = models.FloatField(verbose_name='毛重', blank=True,null=True)
    staff = models.CharField(verbose_name='操作人员', blank=True, max_length=8)  ###??
    notes = models.TextField(verbose_name='备注', blank=True,max_length=200)
    f_date = models.DateField(verbose_name='创建时间', default=timezone.now)
    belong = models.IntegerField(verbose_name='羊场域')

    def house(self):
        pid = HouseInfo.objects.filter(id=self.house_id).values("pid").first()['pid']
        if pid!=0:
            house = HouseInfo.objects.filter(id=pid).values("name").first()['name']+'-' + HouseInfo.objects.filter(id=self.house_id).values("name").first()['name']
        else:
            house = HouseInfo.objects.filter(id=self.house_id).values("name").first()['name']
        return house
    class Meta:
        verbose_name_plural='剪毛信息'
        verbose_name='剪毛信息'
class sportsInfo(models.Model):
    basic_id = models.IntegerField(verbose_name='羊基本信息id')
    ###!
    exercise_time = models.CharField(verbose_name='运动时间', blank=True,max_length=10)  ##?单位时还是分
    exercise = models.FloatField(verbose_name='米', blank=True,null=True)
    date=models.DateField(verbose_name='日期',blank=True,null=True,default=timezone.now)
    ###!
    belong = models.IntegerField(verbose_name='羊场域')
    def ele_id(self):
        basic=BasicInfo.objects.filter(id=self.basic_id).values("ele_num")
        basic_ele=basic[0]['ele_num']
        return basic_ele
    class Meta:
        verbose_name_plural='运动数据'
        verbose_name='运动数据'
class productivityInfo(models.Model):
    basic_id = models.IntegerField(verbose_name='羊基本信息id')

    weight = models.FloatField(verbose_name='体重', blank=True,null=True)
    high = models.FloatField(verbose_name='体高', blank=True,null=True)
    Llong = models.FloatField(verbose_name='斜体长', blank=True,null=True)
    bust = models.FloatField(verbose_name='胸围', blank=True,null=True)
    month_age = models.FloatField(verbose_name='月龄', blank=True,null=True)
    ##!
    fecundity =models.IntegerField(verbose_name='繁殖力id',blank=True,null=True)
    per_meat =models.IntegerField(verbose_name='产肉性能',blank=True,null=True)
    per_milk =models.IntegerField(verbose_name='泌乳性高',blank=True,null=True)
    per_hair =models.IntegerField(verbose_name='产毛性能',blank=True,null=True)
    per_skin =models.IntegerField(verbose_name='产皮性能',blank=True,null=True)
    ##!
    growth_rate = models.CharField(verbose_name='生长速度', blank=True,max_length=10)
    FCR = models.FloatField(verbose_name='饲料转化率', blank=True,null=True)
    belong = models.IntegerField(verbose_name='羊场域')
    def ele_id(self):
        basic=BasicInfo.objects.filter(id=self.basic_id).values("ele_num")
        basic_ele=basic[0]['ele_num']
        return basic_ele
    class Meta:
        verbose_name_plural='生产性能详细'
        verbose_name='生产性能详细'

class milkperformance(models.Model):
    basic_id=models.IntegerField(verbose_name='羊基本信息id',blank=True)
    milk_volume=models.CharField(verbose_name='奶量',blank=True,max_length=40)
    lamb_num=models.IntegerField(verbose_name='产羔数',blank=True,null=True)
    date=models.DateField(verbose_name='登记时间',blank=True)
    f_staff=models.CharField(verbose_name='创建人员',blank=True,null=True,max_length=20)

    belong = models.IntegerField(verbose_name='羊场域')
    def ele_id(self):
        basic=BasicInfo.objects.filter(id=self.basic_id).values("ele_num")
        basic_ele=basic[0]['ele_num']
        return basic_ele
    class Meta:
        verbose_name='泌乳性能'
        verbose_name_plural='泌乳性能'

class skinperformance(models.Model):
    basic_id=models.IntegerField(verbose_name='羊基本信息id')
    skin_area=models.FloatField(verbose_name='皮面积',blank=True,null=True)
    skin_thick=models.FloatField(verbose_name='皮厚度',blank=True,null=True)
    date=models.DateField(verbose_name='登记时间',blank=True)
    f_staff=models.CharField(verbose_name='创建人员',blank=True,null=True,max_length=20)
    belong = models.IntegerField(verbose_name='羊场域')
    def ele_id(self):
        basic=BasicInfo.objects.filter(id=self.basic_id).values("ele_num")
        basic_ele=basic[0]['ele_num']
        return basic_ele
    class Meta:
        verbose_name='产皮性能'
        verbose_name_plural='产皮性能'
