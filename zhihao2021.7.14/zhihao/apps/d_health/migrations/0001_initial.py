# Generated by Django 3.0.7 on 2020-09-26 13:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='deathInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_id', models.IntegerField(verbose_name='羊基本信息id')),
                ('date', models.DateField(blank=True, verbose_name='死亡日期')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='年龄')),
                ('cause', models.IntegerField(choices=[(0, '疾病'), (1, '其他')], verbose_name='死亡原因')),
                ('harmless_treatment', models.IntegerField(choices=[(0, '深埋'), (1, '高温热炼'), (2, '第三方')], verbose_name='无害化处理')),
                ('t_time', models.DateField(blank=True, verbose_name='处理时间')),
                ('t_staff', models.CharField(blank=True, max_length=8, verbose_name='处理人')),
                ('f_staff', models.CharField(blank=True, max_length=20, null=True, verbose_name='创建人')),
                ('f_date', models.DateField(blank=True, verbose_name='创建时间')),
                ('notes', models.TextField(blank=True, max_length=200, verbose_name='备注')),
                ('belong', models.IntegerField(verbose_name='羊场域')),
            ],
            options={
                'verbose_name': '死亡信息',
                'verbose_name_plural': '死亡信息',
            },
        ),
        migrations.CreateModel(
            name='diseaseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_id', models.IntegerField(verbose_name='羊基本信息id')),
                ('disease_time', models.DateField(blank=True, verbose_name='发病时间')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='年龄')),
                ('disease', models.CharField(blank=True, max_length=30, verbose_name='疾病名称')),
                ('treatment_time', models.DateField(blank=True, verbose_name='诊疗时间')),
                ('m_staff', models.CharField(blank=True, max_length=8, verbose_name='诊疗人员')),
                ('drug_id', models.IntegerField(blank=True,null=True, verbose_name='治疗药物')),
                ('drug_type', models.CharField(blank=True, max_length=20, verbose_name='是否国家允许的药物（药物类型）')),
                ('WDT', models.CharField(blank=True, max_length=20, verbose_name='休药期')),
                ('cur_effect', models.IntegerField(blank=True, choices=[(0, '治愈'), (1, '淘汰'), (2, '死亡')], verbose_name='治愈效果')),
                ('cur_time', models.DateField(blank=True, verbose_name='治愈时间')),
                ('out_time', models.DateField(blank=True, verbose_name='出库时间')),
                ('out_no', models.IntegerField(blank=True, null=True, verbose_name='出库编号')),
                ('f_staff', models.IntegerField(blank=True, null=True, verbose_name='创建人员')),
                ('belong', models.IntegerField(verbose_name='羊场域')),
            ],
            options={
                'verbose_name': '疾病信息',
                'verbose_name_plural': '疾病信息',
            },
        ),
        migrations.CreateModel(
            name='drugbathInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_id', models.IntegerField(verbose_name='羊基本信息id')),
                ('drug_age', models.FloatField(blank=True, null=True, verbose_name='药浴月龄')),
                ('take_time', models.DateField(blank=True, verbose_name='用药时间')),
                ('drug_id', models.IntegerField(blank=True, null=True, verbose_name='药品信息(出库)')),
                ('vac_maker', models.IntegerField(blank=True, null=True, verbose_name='药物厂家')),
                ('effect', models.TextField(blank=True, max_length=200, verbose_name='作用')),
                ('timing', models.CharField(blank=True, max_length=20, verbose_name='药效时间')),
                ('IR_bath', models.CharField(blank=True, max_length=40, verbose_name='驱虫药浴')),
                ('out_time', models.DateField(blank=True, verbose_name='出库时间')),
                ('f_date', models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='创建时间')),
                ('operators', models.CharField(blank=True, max_length=8, verbose_name='操作员')),
                ('belong', models.IntegerField(verbose_name='羊场域')),
            ],
            options={
                'verbose_name_plural': '药浴免疫',
            },
        ),
        migrations.CreateModel(
            name='ImmunizationInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_id', models.IntegerField(verbose_name='羊基本信息id')),
                ('imm_age', models.FloatField(blank=True, null=True, verbose_name='接种月龄')),
                ('imm_date', models.DateField(blank=True, null=True, verbose_name='接种日期')),
                ('vaccine_id', models.IntegerField(blank=True, null=True, verbose_name='疫苗信息')),
                ('maker_id', models.IntegerField(blank=True, null=True, verbose_name='疫苗厂家')),
                ('dose', models.CharField(blank=True, max_length=20, null=True, verbose_name='剂量')),
                ('anti_level', models.CharField(blank=True, max_length=40, null=True, verbose_name='抗体水平监测')),
                ('post_stage', models.CharField(blank=True, max_length=40, null=True, verbose_name='阶段后监测')),
                ('out_time', models.DateField(verbose_name='出库时间')),
                ('f_date', models.DateField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('operators', models.TextField(blank=True, max_length=200, verbose_name='操作')),
                ('belong', models.IntegerField(verbose_name='羊场域')),
            ],
            options={
                'verbose_name_plural': '接种免疫',
            },
        ),
        migrations.CreateModel(
            name='nursingInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_id', models.IntegerField(verbose_name='羊基本信息id')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='年龄')),
                ('nurse', models.CharField(blank=True, max_length=8, verbose_name='护理人员')),
                ('nur_time', models.DateField(blank=True, verbose_name='护理时间')),
                ('testis_shape', models.BooleanField(choices=[(True, '正常'), (False, '不正常')], verbose_name='睾丸形状')),
                ('prenatal_paralysi', models.BooleanField(choices=[(True, '是'), (False, '否')], verbose_name='产前瘫痪')),
                ('uterus_fall', models.BooleanField(choices=[(True, '是'), (False, '否')], verbose_name='子宫脱落')),
                ('swelling', models.BooleanField(choices=[(True, '是'), (False, '否')], verbose_name='乳房肿胀')),
                ('Ab_color', models.IntegerField(blank=True, choices=[(0, '黄'), (1, '百'), (2, '红'), (3, '绿')], verbose_name='产后胎衣颜色')),
                ('Ab_smell', models.IntegerField(blank=True, choices=[(0, '正常'), (1, '血腥'), (2, '血臭')], verbose_name='产后胎衣颜色')),
                ('information', models.TextField(blank=True, max_length=200, verbose_name='情况说明')),
                ('f_date', models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='创建时间')),
                ('belong', models.IntegerField(verbose_name='羊场域')),
            ],
            options={
                'verbose_name_plural': '护理信息',
            },
        ),
        migrations.CreateModel(
            name='quarantineInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_id', models.IntegerField(verbose_name='羊基本信息id')),
                ('date', models.DateField(blank=True, verbose_name='采样日期')),
                ('detection_mode', models.IntegerField(blank=True, choices=[(0, '尿检'), (1, '血检')], verbose_name='检测方式')),
                ('item', models.CharField(blank=True, max_length=20, verbose_name='检测项目')),
                ('num', models.IntegerField(blank=True, null=True, verbose_name='采样数量')),
                ('antibody', models.CharField(blank=True, max_length=40, verbose_name='抗体')),
                ('institutions', models.CharField(blank=True, default='自检', max_length=20, verbose_name='检测单位')),
                ('third_name', models.CharField(blank=True, max_length=30, verbose_name='第三方名称')),
                ('inspector', models.CharField(blank=True, max_length=8, verbose_name='检测人员')),
                ('result1', models.IntegerField(blank=True, choices=[(0, '瘦肉精(合格)'), (1, '瘦肉精(不合格)')], verbose_name='监测结果1')),
                ('result2', models.IntegerField(blank=True, choices=[(0, '布病(阴性)'), (1, '布病(阳性)')], verbose_name='监测结果2')),
                ('result3', models.IntegerField(blank=True, choices=[(0, '测孕(阴性)'), (1, '测孕(阳性)')], verbose_name='监测结果3')),
                ('situation', models.IntegerField(blank=True, choices=[(0, '允许销售'), (1, '不允许销售'), (2, '治疗'), (3, '淘汰')], verbose_name='处理情况')),
                ('attachment', models.ImageField(blank=True, upload_to='images/attachment/%Y%m%d', verbose_name='附件')),
                ('notes', models.TextField(blank=True, max_length=200, verbose_name='备注')),
                ('belong', models.IntegerField(verbose_name='羊场域')),
            ],
            options={
                'verbose_name_plural': '检疫检验',
            },
        ),
    ]