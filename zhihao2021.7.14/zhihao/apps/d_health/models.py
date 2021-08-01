from django.db import models
from django.utils import timezone
from apps.basic.models import BasicInfo
from apps.supply.models import v_suppliersInfo
from apps.supply.models import commodityInfo
# Create your models here.
class ImmunizationInfo(models.Model):
    basic_id=models.IntegerField(verbose_name='羊基本信息id')
    ##！
    imm_age=models.FloatField(verbose_name='接种月龄',blank=True,null=True)
    imm_date=models.DateField(verbose_name='接种日期',blank=True,null=True,default=timezone.now)
    ##！
    vaccine_id=models.IntegerField(verbose_name='疫苗信息',blank=True,null=True)
    maker_id=models.IntegerField(verbose_name='疫苗厂家',blank=True,null=True)
    ##!
    dose=models.CharField(verbose_name='剂量',max_length=20,blank=True,null=True)
    anti_level=models.CharField(verbose_name='抗体水平监测',max_length=40,blank=True,null=True)
    post_stage=models.CharField(verbose_name='阶段后监测',max_length=40,blank=True,null=True)

    out_time=models.DateField(verbose_name='出库时间',default=timezone.now)
    ##!
    f_date=models.DateField(verbose_name='创建时间',default=timezone.now)
    f_staff = models.CharField(verbose_name='创建人员', blank=True, null=True, max_length=20)
    ##!
    operators=models.TextField(verbose_name='操作',blank=True,max_length=200)
    belong = models.IntegerField(verbose_name='羊场域')
    def ele_id(self):
        basic=BasicInfo.objects.filter(id=self.basic_id).values("ele_num")
        basic_ele=basic[0]['ele_num']
        return basic_ele
    def pre_num(self):
        basic = BasicInfo.objects.filter(id=self.basic_id).first()
        return basic.pre_num if basic else '-'
    def maker(self):
        maker=v_suppliersInfo.objects.filter(id=self.maker_id).values("supplier_name").first()
        return maker['supplier_name'] if maker else '-'
    def vaccine(self):
        vaccine=commodityInfo.objects.filter(id=self.vaccine_id).values("cname").first()
        return vaccine['cname'] if vaccine else '-'
    class Meta:
        verbose_name_plural='接种免疫'
        verbose_name = '接种免疫'
class drugbathInfo(models.Model):
    basic_id=models.IntegerField(verbose_name='羊基本信息id')

    drug_age=models.FloatField(verbose_name='药浴月龄',blank=True,null=True)##??派生属性？

    take_time=models.DateField(verbose_name='用药时间',blank=True,null=True,default=timezone.now)##春秋各一次，是否用Date

    drug_id=models.IntegerField(verbose_name='药品信息',blank=True,null=True)
    vac_maker=models.IntegerField(verbose_name='药物厂家',blank=True,null=True)

    effect=models.TextField(verbose_name='作用',blank=True,max_length=200)
    timing=models.CharField(verbose_name='药效时间',blank=True,max_length=20)##???是否按截止时间，还是需要时间

    IR_bath=models.CharField(verbose_name='驱虫药浴',blank=True,max_length=40)##??这个是是否，还是药浴名称，需要多长

    out_time=models.DateField(verbose_name='出库时间',default=timezone.now)
    f_date=models.DateField(verbose_name='创建时间',default=timezone.now)
    f_staff = models.CharField(verbose_name='创建人员', blank=True, null=True, max_length=20)
    operators=models.CharField(verbose_name='操作员',blank=True,max_length=8)###员工名还是号
    belong = models.IntegerField(verbose_name='羊场域')
    def ele_id(self):
        basic=BasicInfo.objects.filter(id=self.basic_id).values("ele_num").first()
        return basic['ele_num']
    def pre_num(self):
        basic = BasicInfo.objects.filter(id=self.basic_id).first()
        return basic.pre_num if basic else '-'
    def drug_maker(self):
        maker=v_suppliersInfo.objects.filter(id=self.vac_maker).values("supplier_name").first()
        return maker['supplier_name'] if maker else '-'
    def drug(self):
        drug=commodityInfo.objects.filter(id=self.drug_id).values("cname").first()
        return drug['cname'] if drug else '-'
    class Meta:
        verbose_name_plural='药浴消毒'
        verbose_name = '药浴消毒'
class quarantineInfo(models.Model):
    basic_id=models.IntegerField(verbose_name='羊基本信息id')
    date=models.DateField(verbose_name='采样日期',blank=True,null=True,default=timezone.now)

    detection_mode_choice=((0,'尿检'),(1,'血检'))
    detection_mode=models.IntegerField(verbose_name='检测方式',blank=True,null=True,choices=detection_mode_choice)

    item=models.CharField(verbose_name='检测项目',max_length=20,blank=True)##是否单选
    quarantine_certificate_no=models.CharField(verbose_name='检疫证号',max_length=20,blank=True)

    num=models.IntegerField(verbose_name='采样数量',blank=True,null=True)
    antibody=models.CharField(verbose_name='抗体',blank=True,max_length=40)###抗体是何？？？？

    institutions=models.CharField(verbose_name='检测单位',blank=True,max_length=20,default='自检')
    third_name=models.CharField(verbose_name='第三方名称',blank=True,max_length=30)###长度是否合适
    inspector=models.CharField(verbose_name='检测人员',blank=True,max_length=8)###人员？？？身份证？员工号？？姓名？？？
    result1_choice=((0,'瘦肉精(合格)'),(1,'瘦肉精(不合格)'))
    result1=models.IntegerField(verbose_name='监测结果1',choices=result1_choice,blank=True,null=True)

    result2_chocie=((0,'布病(阴性)'),(1,'布病(阳性)'))
    result2=models.IntegerField(verbose_name='监测结果2',choices=result2_chocie,blank=True,null=True)

    result3_choice=((0,'测孕(阴性)'),(1,'测孕(阳性)'))
    result3=models.IntegerField(verbose_name='监测结果3',blank=True,choices=result3_choice,null=True)

    situation_choice=((0,'允许销售'),(1,'不允许销售'),(2,'治疗'),(3,'淘汰'))
    situation=models.IntegerField(verbose_name='处理情况',blank=True,choices=situation_choice,null=True)

    attachment=models.ImageField(verbose_name='附件',blank=True,upload_to='images/attachment/%Y%m%d')##文件或照片？？
    notes=models.TextField(verbose_name='备注',blank=True,max_length=200)
    f_staff = models.CharField(verbose_name='创建人员', blank=True, null=True, max_length=20)
    belong = models.IntegerField(verbose_name='羊场域')
    def ele_id(self):
        basic=BasicInfo.objects.filter(id=self.basic_id).values("ele_num")
        basic_ele=basic[0]['ele_num']
        return basic_ele
    def pre_num(self):
        basic = BasicInfo.objects.filter(id=self.basic_id).first()
        return basic.pre_num if basic else '-'
    class Meta:
        verbose_name_plural='检疫检验'
        verbose_name = '检疫检验'
class nursingInfo(models.Model):
    basic_id=models.IntegerField(verbose_name='羊基本信息id')
    age=models.IntegerField(verbose_name='年龄',blank=True,null=True)
    nurse=models.CharField(verbose_name='护理人员',blank=True,max_length=8)
    nur_time=models.DateField(verbose_name='护理时间',blank=True,null=True,default=timezone.now)
    drug_id = models.IntegerField(verbose_name='护理使用药品', blank=True, null=True)
    dose=models.CharField(verbose_name='剂量',max_length=20,blank=True,null=True)
    vac_maker = models.IntegerField(verbose_name='药品厂家', blank=True, null=True)
    testis_shape_choice=((True,'正常'),(False,'不正常'))
    testis_shape=models.BooleanField(verbose_name='睾丸形状',choices=testis_shape_choice,blank=True,null=True)
    ###!是否都是是否选择
    prenatal_paralysi_choice=((True,'是'),(False,'否'))
    prenatal_paralysi=models.BooleanField(verbose_name='产前瘫痪',choices=prenatal_paralysi_choice,blank=True,null=True)

    uterus_fall_choice=((True,'是'),(False,'否'))
    uterus_fall=models.BooleanField(verbose_name='子宫脱落',choices=uterus_fall_choice,blank=True,null=True)

    swelling_choice=((True,'是'),(False,'否'))
    swelling=models.BooleanField(verbose_name='乳房肿胀',choices=swelling_choice,blank=True,null=True)
    ###!
    Ab_color_choice=((0,'黄'),(1,'百'),(2,'红'),(3,'绿'))
    Ab_color=models.IntegerField(verbose_name='产后胎衣颜色',blank=True,choices=Ab_color_choice,null=True)

    Ab_smell_choice=((0,'正常'),(1,'血腥'),(2,'血臭'))
    Ab_smell=models.IntegerField(verbose_name='产后胎衣气味',choices=Ab_smell_choice,blank=True,null=True)

    information=models.TextField(verbose_name='情况说明',blank=True,max_length=200)
    f_date=models.DateField(verbose_name='创建时间',default=timezone.now)
    f_staff = models.CharField(verbose_name='创建人员', blank=True, null=True, max_length=20)
    belong = models.IntegerField(verbose_name='羊场域')
    def ele_id(self):
        basic=BasicInfo.objects.filter(id=self.basic_id).values("ele_num")
        basic_ele=basic[0]['ele_num']
        return basic_ele
    def pre_num(self):
        basic = BasicInfo.objects.filter(id=self.basic_id).first()
        return basic.pre_num if basic else '-'
    class Meta:
        verbose_name_plural='护理信息'
        verbose_name= '护理信息'

class diseaseInfo(models.Model):
    basic_id=models.IntegerField(verbose_name='羊基本信息id')
    disease_time=models.DateField(verbose_name='发病时间',blank=True,null=True)
    age=models.IntegerField(verbose_name='年龄',blank=True,null=True)
    disease=models.CharField(verbose_name='疾病名称',blank=True,max_length=30)

    treatment_time=models.DateField(verbose_name='诊疗时间',blank=True,null=True)
    m_staff=models.CharField(verbose_name='诊疗人员',blank=True,max_length=8)
    drug_id=models.IntegerField(verbose_name='治疗药物',blank=True,null=True)
    #####???是否是选择

    drug_type=models.CharField(verbose_name='是否国家允许的药物',max_length=20,blank=True)
    ###截止时间还是中间的时间
    WDT=models.CharField(verbose_name='休药期',blank=True,max_length=20)

    cur_effect_choice=((0,'治愈'),(1,'淘汰'),(2,'死亡'))
    cur_effect=models.IntegerField(verbose_name='治愈效果',blank=True,choices=cur_effect_choice,null=True)
    cur_time=models.DateField(verbose_name='治愈时间',blank=True,null=True)

    out_time=models.DateField(verbose_name='出库时间',blank=True,null=True)

    ####单选内容不全
    #out_no_choice=((0,'01原料'),)
    out_no=models.IntegerField(verbose_name='出库编号',blank=True,null=True)
    f_staff=models.CharField(verbose_name='创建人员',blank=True,null=True,max_length=20)###默认诊疗人员
    belong = models.IntegerField(verbose_name='羊场域')
    def ele_id(self):
        basic=BasicInfo.objects.filter(id=self.basic_id).values("ele_num")
        basic_ele=basic[0]['ele_num']
        return basic_ele
    def pre_num(self):
        basic = BasicInfo.objects.filter(id=self.basic_id).first()
        return basic.pre_num if basic else '-'
    def drug(self):
        drug=commodityInfo.objects.filter(id=self.drug_id).values("cname").first()
        return drug['cname'] if drug else '-'
    class Meta:
        verbose_name='疾病信息'
        verbose_name_plural='疾病信息'

class deathInfo(models.Model):
    basic_id=models.IntegerField(verbose_name='羊基本信息id')
    date=models.DateField(verbose_name='死亡日期',blank=True)
    age=models.IntegerField(verbose_name='年龄',blank=True,null=True)
    ####其他的
    cause_choice=((0,'疾病'),(1,'其他'))
    cause=models.IntegerField(verbose_name='死亡原因',choices=cause_choice)

    harmless_treatment_choice=((0,'深埋'),(1,'高温热炼'),(2,'第三方'))
    harmless_treatment=models.IntegerField(verbose_name='无害化处理',choices=harmless_treatment_choice)
    t_time=models.DateField(verbose_name='处理时间',blank=True)
    t_staff=models.CharField(verbose_name='处理人',max_length=8,blank=True)
    f_staff=models.CharField(verbose_name='创建人员',blank=True,null=True,max_length=20)
    f_date=models.DateField(verbose_name='创建时间',blank=True)
    notes=models.TextField(verbose_name='备注',blank=True,max_length=200)
    belong = models.IntegerField(verbose_name='羊场域')
    def ele_id(self):
        basic=BasicInfo.objects.filter(id=self.basic_id).values("ele_num")
        basic_ele=basic[0]['ele_num']
        return basic_ele
    def pre_num(self):
        basic = BasicInfo.objects.filter(id=self.basic_id).first()
        return basic.pre_num if basic else '-'
    class Meta:
        verbose_name='死亡信息'
        verbose_name_plural='死亡信息'
