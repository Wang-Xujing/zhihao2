# Generated by Django 3.0.7 on 2021-06-19 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0009_auto_20210619_1602'),
        ('d_health', '0008_auto_20210411_1101'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='drugbathinfo',
            options={'verbose_name': '药浴免疫', 'verbose_name_plural': '药浴免疫'},
        ),
        migrations.AlterModelOptions(
            name='immunizationinfo',
            options={'verbose_name': '接种免疫', 'verbose_name_plural': '接种免疫'},
        ),
        migrations.AlterModelOptions(
            name='quarantineinfo',
            options={'verbose_name': '检疫检验', 'verbose_name_plural': '检疫检验'},
        ),
        migrations.AlterField(
            model_name='drugbathinfo',
            name='basic_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='basic.BasicInfo', verbose_name='羊只基本信息'),
        ),
        migrations.AlterField(
            model_name='nursinginfo',
            name='Ab_smell',
            field=models.IntegerField(blank=True, choices=[(0, '正常'), (1, '血腥'), (2, '血臭')], null=True, verbose_name='产后胎衣气味'),
        ),
    ]