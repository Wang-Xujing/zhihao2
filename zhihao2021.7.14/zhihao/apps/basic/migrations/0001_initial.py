# Generated by Django 3.0.7 on 2020-09-26 13:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ele_num', models.CharField(max_length=16, unique=True, verbose_name='电子耳号')),
                ('pre_num', models.CharField(blank=True, max_length=16, unique=True, verbose_name='防疫耳号')),
                ('purpose', models.IntegerField(choices=[(0, '育苗'), (1, '育肥')], verbose_name='用途')),
                ('variety', models.IntegerField(blank=True, choices=[(0, '湖羊'), (1, '小尾'), (2, '黑山'), (3, '小尾3'), (4, '小尾4'), (5, '小尾5'), (6, '小尾6')], verbose_name='品种')),
                ('sex', models.IntegerField(choices=[(0, '母'), (1, '公')], verbose_name='性别')),
                ('manu_info_id', models.IntegerField(blank=True, null=True, verbose_name='源产地id')),
                ('manu_info_name', models.CharField(blank=True, max_length=50, verbose_name='产地名')),
                ('state', models.IntegerField(choices=[(0, '正常'), (1, '销售'), (2, '死亡')], verbose_name='状态')),
                ('birth', models.DateField(default=django.utils.timezone.now, verbose_name='出生日期')),
                ('bir_weight', models.FloatField(blank=True, null=True, verbose_name='出生重(kg)')),
                ('wea_weight', models.FloatField(blank=True, null=True, verbose_name='断奶重(kg)')),
                ('house_id', models.IntegerField(blank=True, null=True, verbose_name='圈舍号')),
                ('hurdle_id', models.IntegerField(blank=True, null=True, verbose_name='圈栏号')),
                ('house_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='圈栏名称')),
                ('hurdle_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='圈舍名称')),
                ('mon_age', models.FloatField(blank=True, null=True, verbose_name='月龄')),
                ('father_id', models.IntegerField(blank=True, null=True, verbose_name='父ID')),
                ('mother_id', models.IntegerField(blank=True, null=True, verbose_name='母ID')),
                ('f_ele_num', models.CharField(blank=True, max_length=16, null=True, verbose_name='父电子耳号')),
                ('f_pre_num', models.CharField(blank=True, max_length=16, null=True, verbose_name='父防疫耳号')),
                ('m_ele_num', models.CharField(blank=True, max_length=16, null=True, verbose_name='母电子耳号')),
                ('m_pre_num', models.CharField(blank=True, max_length=16, null=True, verbose_name='母防疫耳号')),
                ('f_staff', models.CharField(blank=True, max_length=20, null=True, verbose_name='创建人员')),
                ('f_date', models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='创建时间')),
                ('img_positive', models.ImageField(blank=True, upload_to='images/pos/%Y/%m/%d', verbose_name='正面照片')),
                ('img_left', models.ImageField(blank=True, upload_to='images/left/%Y/%m/%d', verbose_name='左侧照片')),
                ('img_right', models.ImageField(blank=True, upload_to='images/right/%Y/%m/%d', verbose_name='右侧照片')),
                ('note', models.TextField(blank=True, max_length=300, null=True, verbose_name='备注信息')),
                ('belong', models.IntegerField(verbose_name='羊场域')),
            ],
            options={
                'verbose_name': '养只基本信息',
                'verbose_name_plural': '养只基本信息',
                'ordering': ('-f_date',),
            },
        ),
        migrations.CreateModel(
            name='BreederconditionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='测量日期')),
                ('basic_id', models.IntegerField(verbose_name='羊基本信息id')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='年龄')),
                ('high', models.FloatField(blank=True, null=True, verbose_name='体高')),
                ('weight', models.FloatField(blank=True, null=True, verbose_name='体重')),
                ('Llong', models.FloatField(blank=True, null=True, verbose_name='斜体长')),
                ('bust', models.FloatField(blank=True, null=True, verbose_name='胸围')),
                ('testis_shape', models.BooleanField(blank=True, choices=[(True, '正常'), (False, '非正常')], verbose_name='睾丸形状')),
                ('t_staff', models.CharField(blank=True, max_length=8, verbose_name='测量人员')),
                ('AE', models.TextField(blank=True, max_length=200, verbose_name='外貌评定')),
                ('performance_traits', models.CharField(blank=True, max_length=40, verbose_name='生产性能')),
                ('with_births', models.IntegerField(blank=True, null=True, verbose_name='同胎数')),
                ('wea_weight', models.FloatField(blank=True, null=True, verbose_name='断奶重')),
                ('June_heavy', models.FloatField(blank=True, null=True, verbose_name='六月重')),
                ('health', models.CharField(blank=True, max_length=40, verbose_name='健康情况')),
                ('f_date', models.DateField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('f_staff', models.IntegerField(blank=True, null=True, verbose_name='创建人员')),
                ('notes', models.TextField(blank=True, max_length=200, verbose_name='备注')),
                ('belong', models.IntegerField(verbose_name='羊场域')),
            ],
            options={
                'verbose_name_plural': '种羊体况',
            },
        ),
        migrations.CreateModel(
            name='cutInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_id', models.IntegerField(verbose_name='圈舍号')),
                ('ele_quantity', models.IntegerField(blank=True, null=True, verbose_name='羊只数量')),
                ('variety', models.IntegerField(blank=True, choices=[(0, '湖羊'), (1, '小尾'), (2, '黑山'), (3, '小尾3'), (4, '小尾4'), (5, '小尾5'), (6, '小尾6')], verbose_name='品种')),
                ('cut_time', models.IntegerField(choices=[(3, '3月'), (6, '6月'), (9, '9月')], verbose_name='剪毛时间')),
                ('rank', models.IntegerField(blank=True, verbose_name='羊毛类型')),
                ('color', models.IntegerField(blank=True, default=0, verbose_name='毛色')),
                ('weight', models.FloatField(blank=True, null=True, verbose_name='毛重')),
                ('staff', models.CharField(blank=True, max_length=8, verbose_name='操作人员')),
                ('notes', models.TextField(blank=True, max_length=200, verbose_name='备注')),
                ('belong', models.IntegerField(verbose_name='羊场域')),
            ],
            options={
                'verbose_name_plural': '剪毛信息',
            },
        ),
        migrations.CreateModel(
            name='elechangeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_id', models.IntegerField(verbose_name='羊只基本信息id')),
                ('new_num', models.CharField(max_length=16, unique=True, verbose_name='新耳号')),
                ('old_num', models.CharField(max_length=16, unique=True, verbose_name='旧耳号')),
                ('retime', models.DateField(blank=True, verbose_name='更换时间')),
                ('reason', models.TextField(max_length=50, verbose_name='更换原因')),
                ('sheep_type', models.CharField(blank=True, max_length=10, verbose_name='羊只类型')),
                ('house_num', models.IntegerField(blank=True, null=True, verbose_name='圈舍号')),
                ('staff', models.CharField(blank=True, max_length=8, verbose_name='更换人员')),
                ('f_date', models.DateField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('belong', models.IntegerField(verbose_name='羊场域')),
            ],
            options={
                'verbose_name': '耳号更换信息',
                'verbose_name_plural': '耳号更换信息',
            },
        ),
        migrations.CreateModel(
            name='manuInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manu_name', models.CharField(max_length=40, unique=True, verbose_name='厂家名称')),
                ('scale', models.IntegerField(choices=[(0, '国家级'), (1, '省级'), (2, '市级'), (3, '县级')], verbose_name='养殖场规模')),
                ('type', models.IntegerField(choices=[(0, '扩繁场'), (1, '育肥场')], verbose_name='养殖场类型')),
                ('BP_license_num', models.CharField(blank=True, max_length=30, verbose_name='种畜禽经营许可证编号')),
                ('AP_certificate_num', models.CharField(blank=True, max_length=30, verbose_name='动物防疫合格证编号')),
                ('BL_num', models.CharField(blank=True, max_length=30, verbose_name='营业执照编号')),
                ('legal', models.CharField(blank=True, max_length=10, verbose_name='法人')),
                ('address', models.CharField(blank=True, max_length=50, verbose_name='地址')),
                ('contact', models.CharField(blank=True, max_length=15, verbose_name='联系方式')),
                ('province', models.CharField(blank=True, max_length=8, verbose_name='所属省')),
                ('city', models.CharField(blank=True, max_length=8, verbose_name='市/县')),
                ('belong', models.IntegerField(verbose_name='羊场域')),
            ],
            options={
                'verbose_name': '羊只产地信息',
                'verbose_name_plural': '羊只产地信息',
            },
        ),
        migrations.CreateModel(
            name='milkperformance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_id', models.IntegerField(blank=True, verbose_name='羊基本信息id')),
                ('milk_volume', models.CharField(blank=True, max_length=40, verbose_name='奶量')),
                ('lamb_num', models.IntegerField(blank=True, null=True, verbose_name='产羔数')),
                ('date', models.DateField(blank=True, verbose_name='登记时间')),
                ('f_staff', models.IntegerField(blank=True, null=True, verbose_name='创建人员')),
                ('belong', models.IntegerField(verbose_name='羊场域')),
            ],
            options={
                'verbose_name': '泌乳性能',
                'verbose_name_plural': '泌乳性能',
            },
        ),
        migrations.CreateModel(
            name='productivityInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_id', models.IntegerField(verbose_name='羊基本信息id')),
                ('weight', models.FloatField(blank=True, null=True, verbose_name='体重')),
                ('high', models.FloatField(blank=True, null=True, verbose_name='体高')),
                ('Llong', models.FloatField(blank=True, null=True, verbose_name='斜体长')),
                ('bust', models.FloatField(blank=True, null=True, verbose_name='胸围')),
                ('month_age', models.FloatField(blank=True, null=True, verbose_name='月龄')),
                ('fecundity', models.IntegerField(blank=True, null=True, verbose_name='繁殖力id')),
                ('per_meat', models.IntegerField(blank=True, null=True, verbose_name='产肉性能')),
                ('per_milk', models.IntegerField(blank=True, null=True, verbose_name='泌乳性高')),
                ('per_hair', models.IntegerField(blank=True, null=True, verbose_name='产毛性能')),
                ('per_skin', models.IntegerField(blank=True, null=True, verbose_name='产皮性能')),
                ('growth_rate', models.CharField(blank=True, max_length=10, verbose_name='生长速度')),
                ('FCR', models.FloatField(blank=True, null=True, verbose_name='饲料转化率')),
                ('belong', models.IntegerField(verbose_name='羊场域')),
            ],
            options={
                'verbose_name_plural': '生产性能详细',
            },
        ),
        migrations.CreateModel(
            name='skinperformance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_id', models.IntegerField(verbose_name='羊基本信息id')),
                ('skin_area', models.FloatField(blank=True, null=True, verbose_name='皮面积')),
                ('skin_thick', models.FloatField(blank=True, null=True, verbose_name='皮厚度')),
                ('date', models.DateField(blank=True, verbose_name='登记时间')),
                ('f_staff', models.IntegerField(blank=True, null=True, verbose_name='创建人员')),
                ('belong', models.IntegerField(verbose_name='羊场域')),
            ],
            options={
                'verbose_name': '产皮性能',
                'verbose_name_plural': '产皮性能',
            },
        ),
        migrations.CreateModel(
            name='sportsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_id', models.IntegerField(verbose_name='羊基本信息id')),
                ('exercise_time', models.CharField(blank=True, max_length=10, verbose_name='运动时间')),
                ('exercise', models.FloatField(blank=True, null=True, verbose_name='米')),
                ('belong', models.IntegerField(verbose_name='羊场域')),
            ],
            options={
                'verbose_name_plural': '运动数据',
            },
        ),
    ]