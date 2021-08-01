from django.db import models
from django.utils import timezone
from apps.basic.models import BasicInfo
from apps.colony.models import HouseInfo
# Create your models here.

# 经济效益表
class economicInfo(models.Model):
    belong = models.CharField(verbose_name='羊场域', max_length=40, default='zhiHao')

    basic_id = models.CharField(verbose_name="羊只基本信息ID", max_length=16)
    age = models.FloatField(verbose_name="年龄",blank=True,null=True)
    house_id= models.IntegerField(verbose_name="圈舍号", blank=True)
    in_weight = models.FloatField(verbose_name="入栏体重",  blank=True,null=True)
    in_1_5 = models.FloatField(verbose_name="入栏1.5月体重",  blank=True,null=True)
    in_3 = models.FloatField(verbose_name="入栏3月体重",  blank=True,null=True)
    in_4_5 = models.FloatField(verbose_name="入栏4.5月体重",  blank=True,null=True)
    out_weight = models.FloatField(verbose_name="出栏体重",  blank=True,null=True)
    put_volume = models.FloatField(verbose_name="投放量（每1.5个月）",  blank=True,null=True)
    intake = models.FloatField(verbose_name="采食量（每1.5个月）",  blank=True,null=True)
    menu = models.FloatField(verbose_name="食物品种",  blank=True,null=True)
    cost = models.FloatField(verbose_name="成本",  blank=True,null=True)
    FCR = models.FloatField(verbose_name="饲料转化率", blank=True,null=True)
    ADG = models.FloatField(verbose_name="日增重",  blank=True,null=True)
    f_staff = models.CharField(verbose_name='创建人员', blank=True, null=True, max_length=20)
    def house(self):
        pid = HouseInfo.objects.filter(id=self.house_id).values("pid").first().get('pid')
        if pid!=0:
            house = HouseInfo.objects.filter(id=pid).values("name").first().get('name')+'-' + HouseInfo.objects.filter(id=self.house_id).values("name").first().get('name')
        else:
            house = HouseInfo.objects.filter(id=self.house_id).values("name").first().get('name')
        return house
    def ele_id(self):
        basic=BasicInfo.objects.filter(id=self.basic_id).values("ele_num").first()
        return basic['ele_num'] if basic else '-'
    def pre_num(self):
        basic = BasicInfo.objects.filter(id=self.basic_id).first()
        return basic.pre_num if basic else '-'
    class Meta:
        verbose_name = '经济效益信息'
        verbose_name_plural = "经济效益信息"

# 羊只销售记录表

class S_salesInfo(models.Model):
    

    sales_date = models.DateField(verbose_name="销售日期", default=timezone.now)
    sales_order = models.CharField(verbose_name="销售单号", max_length=10)

    type_choices = ((0, '羊苗'), (1, '育肥羊'), (2, '种羊'))
    type = models.IntegerField(verbose_name="类型", choices=type_choices)

    quarantine_coding = models.CharField(verbose_name="检疫编码", max_length=20, unique=True)
    ele_num = models.CharField(verbose_name="耳号", max_length=16, unique=True)
    age = models.FloatField(verbose_name="年龄",blank=True,null=True)
    medical_leave = models.BooleanField(verbose_name="是否执行休药期", default=True)
    billing_unit = models.CharField(verbose_name="计费单位", default="kg", max_length=5)
    unit_price = models.FloatField(verbose_name="单价",blank=True,null=True)
    total_price = models.FloatField(verbose_name="总价",blank=True,null=True)

    transportation = models.CharField(verbose_name="运输方式", max_length=15, blank=True)
    img_trans = models.ImageField(verbose_name="运输现场照片", upload_to='images/sheep_trans/%Y/%m/%d', blank=True)

    sales_site = models.TextField(verbose_name="销售地点", max_length=15)
    name = models.CharField(verbose_name="销往单位名称", max_length=10)
    buyer = models.CharField(verbose_name="买方联系人", max_length=5)
    buyer_phone = models.CharField(verbose_name="买方电话", max_length=11)

    selling_choices = ((0, "合作者"), (1, "代理商"), (2, "单位"), (3, "个人"), (4, "餐饮公司"), (5, "商超"), (6, "电商平台"), (7, "社区便利店"))
    selling_type = models.IntegerField(verbose_name="销往对象类型", choices=selling_choices)

    notes = models.TextField(verbose_name="备注信息", max_length=30,  blank=True)
    f_staff = models.CharField(verbose_name='创建人员', blank=True, null=True, max_length=20)
    belong = models.IntegerField(verbose_name='羊场域')
    class Meta:
        ordering = ('-sales_date',)
        verbose_name = '羊只销售信息'
        verbose_name_plural = "羊只销售信息"


# 商品销售记录表

class G_salesInfo(models.Model):
    

    sales_date = models.DateField(verbose_name="销售日期", default=timezone.now)
    sales_order = models.CharField(verbose_name="销售单号", max_length=10)

    type_choices = ((0, '羊粪'), (1, '羊毛'), (2, '羊皮'))
    type = models.IntegerField(verbose_name="类型", choices=type_choices)

    billing_unit = models.CharField(verbose_name="计费单位", max_length=5)
    unit_price = models.FloatField(verbose_name="单价",blank=True,null=True)
    total_price = models.FloatField(verbose_name="总价",blank=True,null=True)

    transportation = models.CharField(verbose_name="运输方式", max_length=15, blank=True)
    img_trans = models.ImageField(verbose_name="运输现场照片", upload_to='images/goods_trans/%Y/%m/%d', blank=True)

    sales_site = models.TextField(verbose_name="销售地点", max_length=15)
    name = models.CharField(verbose_name="销往单位名称", max_length=10)
    buyer = models.CharField(verbose_name="买方联系人", max_length=5)
    buyer_phone = models.CharField(verbose_name="买方电话", max_length=11)

    selling_choices = ((0, "合作者"), (1, "代理商"), (2, "单位"), (3, "个人"), (4, "餐饮公司"), (5, "商超"), (6, "电商平台"), (7, "社区便利店"))
    selling_type = models.IntegerField(verbose_name="销往对象类型", choices=selling_choices)

    notes = models.CharField(verbose_name="备注信息", max_length=30,  blank=True)
    f_staff = models.CharField(verbose_name='创建人员', blank=True, null=True, max_length=20)
    belong = models.IntegerField(verbose_name='羊场域')
    class Meta:
        ordering = ('-sales_date',)
        verbose_name = '其他销售信息'
        verbose_name_plural = "其他销售信息"


# 屠宰分割表

class SlaughterSegmentInfo(models.Model):
    

    basic_id = models.CharField(verbose_name="羊只基本信息ID", max_length=16)
    age = models.FloatField(verbose_name="年龄",blank=True,null=True)
    source = models.CharField(verbose_name="羊只来源", max_length=20)
    in_weight = models.FloatField(verbose_name="入场体重",blank=True,null=True)
    CWT = models.FloatField(verbose_name="胴体重", blank=True,null=True)
    net_meat_weight = models.FloatField(verbose_name="净肉重量", blank=True,null=True)
    spine = models.FloatField(verbose_name="羊脊骨", blank=True,null=True)
    chops_weight = models.FloatField(verbose_name="羊排重量", blank=True,null=True)
    stick_bone_weight = models.FloatField(verbose_name="羊棒骨重量", blank=True,null=True)
    others_weight = models.FloatField(verbose_name="杂骨重量", blank=True,null=True)
    head_weight = models.FloatField(verbose_name="羊头重量", blank=True,null=True)
    blood_weight = models.FloatField(verbose_name="羊血重量", blank=True,null=True)
    skin_weight = models.FloatField(verbose_name="羊皮重量", blank=True,null=True)
    heart_weight = models.FloatField(verbose_name="心脏重量", blank=True,null=True)
    liver_weight = models.FloatField(verbose_name="肝脏重量", blank=True,null=True)
    lungs_weight = models.FloatField(verbose_name="肺脏重量", blank=True,null=True)
    tripe_weight = models.FloatField(verbose_name="羊肚重量", blank=True,null=True)
    hoof_weight = models.FloatField(verbose_name="羊蹄重量", blank=True,null=True)
    L_intestine_weight = models.FloatField(verbose_name="羊大肠重量",blank=True,null=True)
    S_intestine_weight = models.FloatField(verbose_name="羊小肠重量", blank=True,null=True)
    kidney_weight = models.FloatField(verbose_name="肾脏重量", blank=True,null=True)
    white_weight = models.FloatField(verbose_name="羊白重量", blank=True,null=True)
    date = models.DateField(verbose_name="登记时间", default=timezone.now)
    f_staff=models.CharField(verbose_name='创建人员',blank=True,null=True,max_length=20)
    belong = models.IntegerField(verbose_name='羊场域')
    def ele_id(self):
        basic=BasicInfo.objects.filter(id=self.basic_id).values("ele_num").first()
        return basic['ele_num'] if basic else '-'
    class Meta:
        ordering = ('-date',)
        verbose_name = '屠宰分割信息'
        verbose_name_plural = "屠宰分割信息"

# 膘情B超表

class BinformationInfo(models.Model):
    
    date = models.DateField(verbose_name="日期", default=timezone.now)
    month = models.FloatField(verbose_name="羊龄（月）",blank=True,null=True)
    basic_id = models.CharField(verbose_name="羊只基本信息ID", max_length=16)

    variety_choices = ((0, '湖羊'), (1, '小尾寒羊'), (2, '无角道赛特'), (3, '道寒杂交F1'), (4, '白杜泊'), (5, '白萨福克'), (6, '杜湖杂交'),(7,'萨湖杂交'),(8,'杜寒杂交'),(9,'萨寒杂交'),(10,'道湖'))
    variety = models.IntegerField(verbose_name="品种", choices=variety_choices)

    source = models.CharField(verbose_name="羊只来源", max_length=20)
    back_fat_thickness = models.FloatField(verbose_name="背膘厚度CM",blank=True,null=True)
    net_meat_ratio = models.FloatField(verbose_name="估计净肉率",  blank=True,null=True)
    CWT = models.FloatField(verbose_name="胴体重量",  blank=True,null=True)
    emuscle_area = models.FloatField(verbose_name="眼肌面积Cm^2",  blank=True,null=True)
    back_thickness = models.FloatField(verbose_name="背部厚度",  blank=True,null=True)
    level = models.CharField(verbose_name="级别",  max_length=10, blank=True)
    recorder = models.CharField(verbose_name="记录员",  max_length=5, blank=True)
    notes = models.TextField(verbose_name="备注信息", max_length=300, blank=True)
    f_staff = models.CharField(verbose_name='创建人员', blank=True, null=True, max_length=20)
    belong = models.IntegerField(verbose_name='羊场域')
    def ele_id(self):
        basic=BasicInfo.objects.filter(id=self.basic_id).values("ele_num").first()
        return basic['ele_num'] if basic else '-'
    class Meta:
        ordering = ('-date',)
        verbose_name = '膘情B超信息'
        verbose_name_plural = "膘情B超信息"





