from django.db import models
from django.utils import timezone
# Create your models here.
class HouseInfo(models.Model):
    pid=models.IntegerField(verbose_name='上级id',blank=True,default=0)
    name=models.CharField(verbose_name='名称',max_length=40,blank=True)
    build_time=models.DateField(verbose_name='建设时间')

    function_choice=((0,'繁殖母羊舍'),(1,'母羊产房'),(2,'母羔哺乳舍'),(3,'育成舍(2月-8月的种羊)'),(4,'种公羊舍'),(5,'育肥羊舍(2月-7个月)'),(6,'隔离羊舍'))
    function=models.IntegerField(verbose_name='功能',choices=function_choice)

    area=models.FloatField(verbose_name='面积',blank=True,null=True)

    h_type_choice=((0,'单排'),(1,'双排'))
    h_type=models.IntegerField(verbose_name='羊舍类型',choices=h_type_choice)
    ##!
    h_lwh=models.CharField(verbose_name='圈舍长宽高',max_length=40,blank=True)
    sports_lwh=models.CharField(verbose_name='运动场长宽高',max_length=40,blank=True)

    sheep_type=models.IntegerField(verbose_name='养羊类型',blank=True,null=True)##?
    sheep_quantity=models.IntegerField(verbose_name='羊只数量',blank=True,null=True)
    area_pro=models.CharField(verbose_name='羊只面积比例',max_length=100,blank=True)
    staff = models.CharField(verbose_name='管理人员', blank=True, max_length=8)
    f_staff = models.CharField(verbose_name='创建人员', blank=True, null=True, max_length=20)
    belong = models.IntegerField(verbose_name='羊场域')
    def peng(self):
        if self.pid==0:
            return '-'
        return HouseInfo.objects.filter(id=self.pid).values('name').first().get('name')

    class Meta:
        verbose_name_plural='圈舍基本信息'
class maintenanceInfo(models.Model):
    house_id=models.IntegerField(verbose_name='圈舍号')

    M_condition=models.TextField(verbose_name='维护情况',blank=True,max_length=200)##??Text是否合适
    M_details=models.TextField(verbose_name='维修内容',blank=True,max_length=200)###??Text是否合适
    M_time=models.DateField(verbose_name='维护时间',blank=True)
    M_cost=models.FloatField(verbose_name='维护成本',blank=True)
    f_date=models.DateField(verbose_name='创建时间',blank=True,default=timezone.now)
    f_staff=models.CharField(verbose_name='创建人员',blank=True,null=True,max_length=20)
    belong = models.IntegerField(verbose_name='羊场域')
    class Meta:
        verbose_name_plural='圈舍维护'
class disinfectionInfo(models.Model):
    house_id=models.IntegerField(verbose_name='圈舍号')

    date=models.DateField(verbose_name='消毒日期',blank=True)
    staff=models.CharField(verbose_name='消毒人员', blank=True, max_length=8)
    drug=models.CharField(verbose_name='消毒药物',blank=True,max_length=50)####50长度是否合适
    dose=models.FloatField(verbose_name='稀释比例(重量/平米)',blank=True,null=True)####能否结尾加%

    method_choice=((0,'喷雾消毒'),(1,'固状消毒'))
    method=models.IntegerField(verbose_name='消毒方法',blank=True,choices=method_choice)###blanks是否合适
    notes=models.TextField(verbose_name='备注',blank=True,max_length=200)
    belong = models.IntegerField(verbose_name='羊场域')
    def house(self):
        pid = HouseInfo.objects.filter(id=self.house_id).values("pid").first()['pid']
        if pid!=0:
            house = HouseInfo.objects.filter(id=pid).values("name").first().get('name')+'-' + HouseInfo.objects.filter(id=self.house_id).values("name").first().get('name')
        else:
            house = HouseInfo.objects.filter(id=self.house_id).values("name").first().get('name')
        return house
    class Meta:
        verbose_name_plural='圈舍消毒信息'
class transferInfo(models.Model):
    basic_id=models.IntegerField(verbose_name='羊基本信息id')

    new_house_id=models.IntegerField(verbose_name='新圈舍号',null=True)
    old_house_id=models.IntegerField(verbose_name='旧圈舍号',null=True)

    reason_choice=((0,'产羔'),(1,'断奶'),(2,'育成'),(3,'疾病'))
    reason=models.IntegerField(verbose_name='转移原因',blank=True,null=True)

    trans_time=models.DateField(verbose_name='转移时间',blank=True)
    sheep_type=models.CharField(verbose_name='羊只类型',blank=True,max_length=20)

    f_date=models.DateField(verbose_name='创建时间',default=timezone.now)
    f_staff=models.CharField(verbose_name='创建人员',blank=True,null=True,max_length=20)
    belong = models.IntegerField(verbose_name='羊场域')
    class Meta:
        verbose_name_plural='圈舍转移'
