# Generated by Django 3.0.7 on 2020-10-21 01:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feeding_out',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outbound_no', models.CharField(max_length=20, unique=True, verbose_name='出库单号')),
                ('type', models.IntegerField(choices=[(2, '草料'), (3, '精料')], verbose_name='类型')),
                ('f_name', models.CharField(max_length=15, verbose_name='饲料名称')),
                ('warehouse_num', models.IntegerField(blank=True, null=True, verbose_name='出库仓库')),
                ('delivery_time', models.DateField(default=django.utils.timezone.now, verbose_name='出库时间')),
                ('out_purposes', models.TextField(verbose_name='出库用途')),
                ('num', models.IntegerField(blank=True, null=True, verbose_name='出库数量')),
                ('out_staff', models.CharField(max_length=5, verbose_name='出库人员')),
                ('maker_id', models.IntegerField(blank=True, null=True, verbose_name='生产厂家id')),
                ('contact_phone', models.CharField(max_length=11, verbose_name='联系电话')),
                ('notes', models.TextField(blank=True, verbose_name='备注信息')),
                ('belong', models.IntegerField(verbose_name='羊场域')),
            ],
            options={
                'verbose_name': '饲料出库信息',
                'verbose_name_plural': '饲料出库信息',
                'ordering': ('-delivery_time',),
            },
        ),
        migrations.CreateModel(
            name='Feedingin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(2, '草料'), (3, '精料')], verbose_name='类型')),
                ('f_name', models.CharField(max_length=15, verbose_name='饲料名称')),
                ('warehouse_num', models.IntegerField(blank=True, null=True, verbose_name='仓库')),
                ('nutrients', models.TextField(blank=True, verbose_name='营养成分')),
                ('buy_time', models.DateField(verbose_name='购买时间')),
                ('billing_unit', models.CharField(default='kg', max_length=3, verbose_name='计费单位')),
                ('quantity', models.FloatField(verbose_name='重量')),
                ('unit_price', models.FloatField(default=1.0, verbose_name='单价（元）')),
                ('total_price', models.FloatField(blank=True, default=0, null=True, verbose_name='总价（元）')),
                ('specifications', models.CharField(blank=True, max_length=15, verbose_name='规格')),
                ('purpose', models.TextField(verbose_name='用途')),
                ('water_content', models.CharField(blank=True, max_length=5, verbose_name='原材料含水量')),
                ('mildew', models.CharField(blank=True, max_length=5, verbose_name='原材料霉变')),
                ('impurity_content', models.CharField(blank=True, max_length=5, verbose_name='原材料杂质含量')),
                ('maker_id', models.IntegerField(blank=True, null=True, verbose_name='生成厂家id')),
                ('notes', models.TextField(blank=True, verbose_name='备注信息')),
                ('f_date', models.DateField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('operation', models.TextField(blank=True, max_length=10, null=True, verbose_name='操作')),
                ('keep_amount', models.IntegerField(blank=True, null=True, verbose_name='库存数量')),
                ('belong', models.IntegerField(verbose_name='羊场域')),
            ],
            options={
                'verbose_name': '饲料入库信息',
                'verbose_name_plural': '饲料入库信息',
                'ordering': ('-f_date',),
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(blank=True, choices=[(0, '疫苗'), (1, '药品'), (2, '草料'), (3, '精料')], null=True, verbose_name='物资类型')),
                ('goods', models.CharField(blank=True, max_length=10, null=True, verbose_name='物资名称')),
                ('maker_id', models.IntegerField(blank=True, null=True, verbose_name='生产厂家id')),
                ('quantity', models.FloatField(blank=True, null=True, verbose_name='库存数量')),
                ('alert', models.FloatField(blank=True, default=1, null=True, verbose_name='警戒数量')),
                ('f_date', models.DateField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('operation', models.TextField(blank=True, max_length=10, null=True, verbose_name='操作')),
                ('belong', models.IntegerField(verbose_name='羊场域')),
                ('out_time', models.DateField(blank=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '物资库存信息',
                'verbose_name_plural': '物资库存信息',
                'ordering': ('-f_date',),
            },
        ),
        migrations.CreateModel(
            name='Vaccine_in',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('v_name', models.CharField(max_length=15, verbose_name='名称')),
                ('type', models.IntegerField(choices=[(0, '疫苗'), (1, '药品')], verbose_name='类别')),
                ('maker_id', models.IntegerField(blank=True, null=True, verbose_name='生产厂家id')),
                ('purpose', models.CharField(blank=True, max_length=30, verbose_name='用途')),
                ('produce_date', models.DateField(verbose_name='生产日期')),
                ('expiration_date', models.DateField(verbose_name='到期日期')),
                ('produce_num', models.CharField(max_length=15, verbose_name='生产批号')),
                ('billing_unit', models.CharField(blank=True, max_length=5, verbose_name='计量单位')),
                ('in_amount', models.IntegerField(verbose_name='入库数量')),
                ('unit_price', models.FloatField(default=1.0, verbose_name='单价（元）')),
                ('total_price', models.FloatField(blank=True, default=0, null=True, verbose_name='总价（元）')),
                ('in_time', models.DateField(verbose_name='入库时间')),
                ('keep_amount', models.IntegerField(blank=True, null=True, verbose_name='库存数量')),
                ('f_date', models.DateField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('operation', models.TextField(blank=True, max_length=20, null=True, verbose_name='操作')),
                ('belong', models.IntegerField(verbose_name='羊场域')),
            ],
            options={
                'verbose_name': '疫苗&药品入库信息',
                'verbose_name_plural': '疫苗&药品入库信息',
                'ordering': ('-f_date',),
            },
        ),
        migrations.CreateModel(
            name='Vaccine_out',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outbound_no', models.CharField(max_length=20, unique=True, verbose_name='出库单号')),
                ('v_name', models.CharField(max_length=20, verbose_name='名称')),
                ('type', models.IntegerField(choices=[(0, '疫苗'), (1, '药品')], verbose_name='类别')),
                ('delivery_time', models.DateField(default=django.utils.timezone.now, verbose_name='出库时间')),
                ('out_purposes', models.TextField(max_length=30, verbose_name='出库用途')),
                ('num', models.IntegerField(blank=True, null=True, verbose_name='出库数量')),
                ('maker_id', models.IntegerField(blank=True, null=True, verbose_name='生产厂家id')),
                ('out_staff', models.CharField(max_length=6, verbose_name='出库人员')),
                ('contact_phone', models.CharField(max_length=11, verbose_name='联系电话')),
                ('notes', models.TextField(blank=True, verbose_name='备注信息')),
                ('belong', models.IntegerField(verbose_name='羊场域')),
            ],
            options={
                'verbose_name': '疫苗&药品出库信息',
                'verbose_name_plural': '疫苗&药品出库信息',
                'ordering': ('-delivery_time',),
            },
        ),
    ]
