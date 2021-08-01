# Generated by Django 3.0.7 on 2021-01-05 05:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArtificialfeedingInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lamb_id', models.IntegerField(verbose_name='羔羊id')),
                ('delivery_date', models.DateField(verbose_name='繁殖日期')),
                ('BW', models.CharField(blank=True, max_length=10, verbose_name='体重监测')),
                ('reason', models.CharField(blank=True, max_length=40, verbose_name='人工喂养原因')),
                ('feeding_material', models.CharField(blank=True, max_length=20, verbose_name='喂养物')),
                ('mcal', models.CharField(blank=True, max_length=20, verbose_name='食量')),
                ('health', models.CharField(blank=True, max_length=10, verbose_name='健康情况')),
                ('help', models.TextField(blank=True, max_length=200, verbose_name='求助情况')),
                ('dose', models.CharField(blank=True, max_length=20, verbose_name='用量')),
                ('feeding_staff', models.CharField(blank=True, max_length=8, verbose_name='喂养人员')),
                ('belong', models.IntegerField(verbose_name='羊场域')),
            ],
            options={
                'verbose_name': '人工喂养',
                'verbose_name_plural': '人工喂养',
            },
        ),
        migrations.CreateModel(
            name='breedingInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breeding_date', models.DateField(blank=True, verbose_name='配种日期')),
                ('pre_production_date', models.DateField(blank=True, verbose_name='预产日期')),
                ('breeding_way', models.IntegerField(choices=[(0, '自然交配'), (1, '人工辅助交配'), (2, '人工授精'), (3, '胚胎移植')], verbose_name='配种方式')),
                ('ewe_id', models.IntegerField(null=True, verbose_name='母羊ID')),
                ('ewe_variety', models.IntegerField(blank=True, choices=[(0, '湖羊'), (1, '小尾寒羊'), (2, '无角道赛特'), (3, '黑羊'), (4, '小尾4'), (5, '小尾5'), (6, '小尾6')], verbose_name='母羊品种')),
                ('ram_id', models.IntegerField(null=True, verbose_name='公羊ID')),
                ('ram_variety', models.IntegerField(blank=True, choices=[(0, '湖羊'), (1, '小尾寒羊'), (2, '无角道赛特'), (3, '黑羊'), (4, '小尾4'), (5, '小尾5'), (6, '小尾6')], verbose_name='公羊品种')),
                ('breeding_state', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], verbose_name='配种状态')),
                ('staff', models.CharField(blank=True, max_length=8, verbose_name='操作师')),
                ('f_staff', models.IntegerField(blank=True, null=True, verbose_name='创建人员')),
                ('f_date', models.DateField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('belong', models.IntegerField(verbose_name='羊场域')),
            ],
            options={
                'verbose_name': '配种信息',
                'verbose_name_plural': '配种信息',
            },
        ),
        migrations.CreateModel(
            name='postnatalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breeding_id', models.IntegerField(blank=True, null=True, verbose_name='配种信息id')),
                ('breeding_date', models.DateField(blank=True, null=True, verbose_name='配种日期')),
                ('delivery_date', models.DateField(blank=True, null=True, verbose_name='分娩日期')),
                ('ram_id', models.IntegerField(blank=True, null=True, verbose_name='公羊耳号')),
                ('ewe_id', models.IntegerField(blank=True, null=True, verbose_name='母羊耳号')),
                ('Booroola', models.FloatField(blank=True, null=True, verbose_name='母羊产羔率')),
                ('ewe_health', models.BooleanField(blank=True, choices=[(True, '正常'), (False, '不正常')], verbose_name='母羊健康情况')),
                ('ewe_condition', models.IntegerField(choices=[(0, '好'), (1, '一般'), (2, '差')], verbose_name='母性情况')),
                ('lamb_ele_num', models.CharField(blank=True, max_length=16, verbose_name='羊羔耳号')),
                ('lamb_state', models.IntegerField(choices=[(0, '健康'), (1, '死亡'), (2, '瘦弱'), (3, '残疾')], verbose_name='羊羔状态')),
                ('bir_weight', models.FloatField(blank=True, null=True, verbose_name='出生体重')),
                ('live_num', models.IntegerField(blank=True, null=True, verbose_name='产羔数')),
                ('birth_attendants', models.CharField(blank=True, max_length=8, verbose_name='接生人员')),
                ('f_staff', models.IntegerField(blank=True, null=True, verbose_name='创建人员')),
                ('f_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='创建时间')),
                ('notes', models.TextField(blank=True, max_length=200, verbose_name='备注')),
                ('belong', models.IntegerField(verbose_name='羊场域')),
            ],
            options={
                'verbose_name': '产后信息',
                'verbose_name_plural': '产后信息',
            },
        ),
        migrations.CreateModel(
            name='pregnantInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_type', models.CharField(max_length=20, verbose_name='检查类别')),
                ('breeding_id', models.IntegerField(verbose_name='羊基本信息id')),
                ('In_pregnancy', models.CharField(blank=True, max_length=40, verbose_name='孕检信息')),
                ('f_staff', models.IntegerField(blank=True, null=True, verbose_name='创建人员')),
                ('f_date', models.DateField(default=django.utils.timezone.now, verbose_name='创建人员')),
                ('notes', models.TextField(blank=True, max_length=200, verbose_name='备注')),
                ('belong', models.IntegerField(verbose_name='羊场域')),
            ],
            options={
                'verbose_name': '孕检信息',
                'verbose_name_plural': '孕检信息',
            },
        ),
        migrations.CreateModel(
            name='rutInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_id', models.IntegerField(verbose_name='羊基本信息id')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='年龄')),
                ('breeding', models.BooleanField(choices=[(True, '是'), (False, '否')], verbose_name='是否配种')),
                ('f_staff', models.IntegerField(blank=True, null=True, verbose_name='创建人员')),
                ('f_date', models.DateField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('belong', models.IntegerField(verbose_name='羊场域')),
            ],
            options={
                'verbose_name': '发情信息',
                'verbose_name_plural': '发情信息',
            },
        ),
        migrations.CreateModel(
            name='SemencollectInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_id', models.IntegerField(verbose_name='羊基本信息id')),
                ('E_date', models.DateField(blank=True, verbose_name='采精日期')),
                ('dilution_ratio', models.FloatField(blank=True, null=True, verbose_name='稀释倍数')),
                ('diluent_type', models.CharField(blank=True, max_length=20, verbose_name='稀释液种类')),
                ('disused', models.BooleanField(choices=[(True, '是'), (False, '否')], verbose_name='是否废弃')),
                ('f_staff', models.IntegerField(blank=True, null=True, verbose_name='创建人员')),
                ('f_date', models.DateField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('belong', models.IntegerField(verbose_name='羊场域')),
            ],
            options={
                'verbose_name': '采精信息',
                'verbose_name_plural': '采精信息',
            },
        ),
        migrations.CreateModel(
            name='weaningInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lamb_id', models.IntegerField(verbose_name='羔羊id')),
                ('Delivery_date', models.DateField(verbose_name='繁殖日期')),
                ('feeding_way', models.IntegerField(choices=[(0, '哺乳'), (1, '人工')], verbose_name='喂养方式')),
                ('Bir_weight', models.FloatField(blank=True, null=True, verbose_name='出生体重')),
                ('wea_weight', models.FloatField(blank=True, null=True, verbose_name='出栏体重(断奶体重)')),
                ('ADR', models.CharField(blank=True, max_length=40, verbose_name='不良反应')),
                ('collection', models.CharField(blank=True, max_length=40, verbose_name='采集量')),
                ('feeding_material', models.CharField(blank=True, max_length=40, verbose_name='喂养食品')),
                ('belong', models.IntegerField(verbose_name='羊场域')),
            ],
            options={
                'verbose_name': '断奶信息',
                'verbose_name_plural': '断奶信息',
            },
        ),
    ]