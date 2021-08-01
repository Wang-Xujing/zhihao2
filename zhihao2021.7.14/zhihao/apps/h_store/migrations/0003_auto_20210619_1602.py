# Generated by Django 3.0.7 on 2021-06-19 16:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('h_store', '0002_auto_20210411_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedingin',
            name='avg_price',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='折合单价'),
        ),
        migrations.AddField(
            model_name='feedingin',
            name='fare',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='运费（元）'),
        ),
        migrations.AddField(
            model_name='vaccine_in',
            name='avg_price',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='折合单价'),
        ),
        migrations.AddField(
            model_name='vaccine_in',
            name='fare',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='运费（元）'),
        ),
        migrations.AlterField(
            model_name='feeding_out',
            name='out_purposes',
            field=models.TextField(blank=True, null=True, verbose_name='出库用途'),
        ),
        migrations.AlterField(
            model_name='feedingin',
            name='purpose',
            field=models.TextField(blank=True, null=True, verbose_name='用途'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='f_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='vaccine_out',
            name='out_purposes',
            field=models.TextField(blank=True, max_length=30, null=True, verbose_name='出库用途'),
        ),
    ]
