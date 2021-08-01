from django.db import models
from django.utils import timezone
from apps.supply.models import v_suppliersInfo
from apps.supply.models import f_suppliersInfo
# Create your models here.

class Vaccine_in(models.Model):

    

    v_name = models.CharField(verbose_name="名称", max_length=15)

    type_choices = ((0, '疫苗'), (1, '药品'))
    type = models.IntegerField(verbose_name="类别", choices=type_choices)
    maker_id = models.IntegerField(verbose_name="生产厂家id", blank=True,null=True)

    purpose = models.CharField(verbose_name="用途", max_length=30, blank=True)
    produce_date = models.DateField(verbose_name="生产日期")
    expiration_date = models.DateField(verbose_name="到期日期")
    produce_num = models.CharField(verbose_name="生产批号", max_length=15)

    billing_unit = models.CharField(verbose_name="计量单位", max_length=5, blank=True)
    in_amount = models.IntegerField(verbose_name="入库数量")
    unit_price = models.FloatField(verbose_name="单价（元）",default=1.0)
    total_price = models.FloatField(verbose_name="总价（元）", default=0,blank=True,null=True)
    fare = models.FloatField(verbose_name="运费（元）", default=0, blank=True, null=True)
    avg_price = models.FloatField(verbose_name="折合单价", default=0, blank=True, null=True)
    in_time = models.DateField(verbose_name="入库时间")
    keep_amount = models.IntegerField(verbose_name="库存数量",blank=True,null=True)
    f_date = models.DateField(verbose_name="创建时间", default=timezone.now)
    f_staff = models.CharField(verbose_name='创建人员', blank=True, null=True, max_length=20)
    operation = models.TextField(verbose_name="操作", max_length=20,blank=True,null=True)
    belong = models.IntegerField(verbose_name="羊场域")
    def maker(self):
        maker=v_suppliersInfo.objects.filter(id=self.maker_id).values("supplier_name").first()
        return maker['supplier_name'] if maker else '-'
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.total_price = self.in_amount * self.unit_price + self.fare
        self.avg_price = self.total_price / self.in_amount
        # 执行 save(), 将数据保存进数据库
        super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields
        )
    class Meta:
        ordering = ('-f_date',)
        verbose_name = '疫苗&药品入库信息'
        verbose_name_plural = "疫苗&药品入库信息"

# 存货清单

class Inventory(models.Model):
    
    type_choices = ((0, '疫苗'), (1, '药品'),(2, '草料'), (3, '精料'))
    type = models.IntegerField(verbose_name="物资类型",blank=True,null=True,choices=type_choices)
    goods = models.CharField(verbose_name="物资名称", max_length=10,blank=True,null=True)
    #manufacturer改为maker_id
    maker_id = models.IntegerField(verbose_name="生产厂家id", blank=True,null=True)
    quantity = models.FloatField(verbose_name="库存数量",blank=True,null=True)
    alert = models.FloatField(verbose_name="警戒数量", default=1,blank=True,null=True)
    f_date = models.DateField(verbose_name="创建时间", default=timezone.now,blank=True,null=True)
    operation = models.TextField(verbose_name="操作", max_length=10,blank=True,null=True)
    f_staff = models.CharField(verbose_name='创建人员', blank=True, null=True, max_length=20)
    belong = models.IntegerField(verbose_name="羊场域")
    out_time=models.DateField(verbose_name="更新时间",blank=True,null=True)
    def maker(self):
        if self.type==0 or self.type==1:
            maker=v_suppliersInfo.objects.filter(id=self.maker_id).values("supplier_name").first()
            return maker['supplier_name'] if maker else '-'
        elif self.type==2 or self.type==3:
            maker = f_suppliersInfo.objects.filter(id=self.maker_id).values("supplier_name").first()
            return maker['supplier_name'] if maker else '-'
        else:
            return '-'
    class Meta:
        ordering = ('-f_date',)
        verbose_name = '物资库存信息'
        verbose_name_plural = "物资库存信息"

# 疫苗、药品入库清单



# 疫苗、药品出库清单

class Vaccine_out(models.Model):


    outbound_no = models.CharField(verbose_name="出库单号", max_length=20, unique=True)
    v_name = models.CharField(verbose_name="名称", max_length=20)

    type_choices = ((0, '疫苗'), (1, '药品'))
    type = models.IntegerField(verbose_name="类别", choices=type_choices)

    delivery_time = models.DateField(verbose_name="出库时间", default=timezone.now)
    out_purposes = models.TextField(verbose_name="出库用途", max_length=30,blank=True,null=True)
    num = models.IntegerField(verbose_name="出库数量",blank=True,null=True)
    maker_id = models.IntegerField(verbose_name="生产厂家id", blank=True, null=True)
    out_staff = models.CharField(verbose_name="出库人员", max_length=6)
    contact_phone = models.CharField(verbose_name="联系电话", max_length=11)
    notes = models.TextField(verbose_name="备注信息", blank=True)
    f_staff = models.CharField(verbose_name='创建人员', blank=True, null=True, max_length=20)
    belong = models.IntegerField(verbose_name="羊场域")
    def maker(self):
        maker=v_suppliersInfo.objects.filter(id=self.maker_id).values("supplier_name").first()
        return maker['supplier_name'] if maker else '-'
    class Meta:
        ordering = ('-delivery_time',)
        verbose_name = '疫苗&药品出库信息'
        verbose_name_plural = "疫苗&药品出库信息"



# 饲料入库清单表

class Feedingin(models.Model):



    type_choices = ((2, '草料'), (3, '精料'))
    type = models.IntegerField(verbose_name="类型", choices=type_choices)

    f_name = models.CharField(verbose_name="饲料名称", max_length=15)
    warehouse_num = models.IntegerField(verbose_name="仓库",blank=True,null=True)
    nutrients = models.TextField(verbose_name="营养成分", blank=True)
    buy_time = models.DateField(verbose_name="购买时间")
    billing_unit = models.CharField(verbose_name="计费单位", max_length=3, default="kg")
    quantity = models.FloatField(verbose_name="重量")
    unit_price = models.FloatField(verbose_name="单价（元）",default=1.0)
    total_price = models.FloatField(verbose_name="总价（元）", default=0,blank=True,null=True)
    fare = models.FloatField(verbose_name="运费（元）", default=0, blank=True, null=True)
    avg_price = models.FloatField(verbose_name="折合单价", default=0, blank=True, null=True)
    specifications = models.CharField(verbose_name="规格", max_length=15, blank=True)
    purpose = models.TextField(verbose_name="用途",blank=True,null=True)
    water_content = models.CharField(verbose_name="原材料含水量", max_length=5, blank=True)
    mildew = models.CharField(verbose_name="原材料霉变", max_length=5, blank=True)
    impurity_content = models.CharField(verbose_name="原材料杂质含量",  max_length=5, blank=True)
    #FI改为maker_id
    maker_id = models.IntegerField(verbose_name="生成厂家id", blank=True,null=True)
    notes = models.TextField(verbose_name="备注信息", blank=True)
    f_date = models.DateField(verbose_name="创建时间", default=timezone.now)
    operation = models.TextField(verbose_name="操作", max_length=10,blank=True,null=True)
    keep_amount = models.IntegerField(verbose_name="库存数量", blank=True, null=True)
    f_staff = models.CharField(verbose_name='创建人员', blank=True, null=True, max_length=20)
    belong = models.IntegerField(verbose_name="羊场域")
    def maker(self):
        maker=f_suppliersInfo.objects.filter(id=self.maker_id).values("supplier_name").first()
        return maker['supplier_name'] if maker else '-'
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.total_price = self.quantity * self.unit_price+self.fare
        self.avg_price=self.total_price/self.quantity

        # 执行 save(), 将数据保存进数据库
        super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields
        )

    class Meta:
        ordering = ('-f_date',)
        verbose_name = '饲料入库信息'
        verbose_name_plural = "饲料入库信息"



# 饲料出库清单表

class Feeding_out(models.Model):


    outbound_no = models.CharField(verbose_name="出库单号", max_length=20, unique=True)

    type_choices = ((2, '草料'), (3, '精料'))
    type = models.IntegerField(verbose_name="类型", choices=type_choices)

    f_name = models.CharField(verbose_name="饲料名称", max_length=15)
    warehouse_num = models.IntegerField(verbose_name="出库仓库",blank=True,null=True)

    delivery_time = models.DateField(verbose_name="出库时间", default=timezone.now)
    out_purposes = models.TextField(verbose_name="出库用途",blank=True,null=True)
    num = models.IntegerField(verbose_name="出库数量",blank=True,null=True)
    out_staff = models.CharField(verbose_name="出库人员", max_length=5)
    maker_id = models.IntegerField(verbose_name="生产厂家id", blank=True, null=True)
    contact_phone = models.CharField(verbose_name="联系电话", max_length=11)
    notes = models.TextField(verbose_name="备注信息", blank=True)
    f_staff = models.CharField(verbose_name='创建人员', blank=True, null=True, max_length=20)
    belong = models.IntegerField(verbose_name="羊场域")
    def maker(self):
        maker=f_suppliersInfo.objects.filter(id=self.maker_id).values("supplier_name").first()
        return maker['supplier_name'] if maker else '-'
    class Meta:
        ordering = ('-delivery_time',)
        verbose_name = '饲料出库信息'
        verbose_name_plural = "饲料出库信息"










