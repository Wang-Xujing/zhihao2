# Generated by Django 3.0.7 on 2020-09-26 13:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='f_suppliersInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.IntegerField(verbose_name='羊场域')),
                ('supplier_name', models.CharField(max_length=20, unique=True, verbose_name='厂商名称')),
                ('sale_type', models.TextField(max_length=50, verbose_name='饲料出售类型')),
                ('sup_linkman', models.CharField(max_length=5, verbose_name='联系人')),
                ('sup_contact', models.CharField(max_length=11, verbose_name='联系人电话')),
                ('contact', models.CharField(blank=True, max_length=11, verbose_name='厂商电话')),
                ('mail', models.CharField(blank=True, max_length=25, verbose_name='邮箱')),
                ('address', models.CharField(max_length=40, verbose_name='地址')),
                ('f_date', models.DateField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('operation', models.TextField(max_length=20, verbose_name='操作')),
            ],
            options={
                'verbose_name': '饲料厂商信息',
                'verbose_name_plural': '饲料厂商信息',
                'ordering': ('-f_date',),
            },
        ),
        migrations.CreateModel(
            name='insuranceinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.IntegerField(verbose_name='羊场域')),
                ('in_name', models.CharField(max_length=20, unique=True, verbose_name='保险公司')),
                ('contact', models.CharField(max_length=11, verbose_name='公司电话')),
                ('mail', models.CharField(blank=True, max_length=25, verbose_name='公司邮箱')),
                ('handler', models.CharField(max_length=5, verbose_name='保险理赔员')),
                ('link', models.CharField(max_length=11, verbose_name='保险员电话')),
                ('f_date', models.DateField(default=django.utils.timezone.now, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '保险公司信息',
                'verbose_name_plural': '保险公司信息',
                'ordering': ('-f_date',),
            },
        ),
        migrations.CreateModel(
            name='v_suppliersInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.IntegerField(verbose_name='羊场域')),
                ('supplier_name', models.CharField(blank=True, max_length=20, verbose_name='厂商名称')),
                ('sale_type', models.TextField(blank=True, max_length=50, verbose_name='疫苗出售类型')),
                ('sup_linkman', models.CharField(blank=True, max_length=5, verbose_name='联系人')),
                ('sup_contact', models.CharField(blank=True, max_length=11, verbose_name='联系人电话')),
                ('contact', models.CharField(blank=True, max_length=11, null=True, verbose_name='厂商电话')),
                ('mail', models.CharField(blank=True, max_length=25, null=True, verbose_name='邮箱')),
                ('address', models.CharField(max_length=40, verbose_name='地址')),
                ('f_date', models.DateField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('operation', models.TextField(max_length=20, verbose_name='操作')),
            ],
            options={
                'verbose_name': '疫苗厂商信息',
                'verbose_name_plural': '疫苗厂商信息',
                'ordering': ('-f_date',),
            },
        ),
    ]
