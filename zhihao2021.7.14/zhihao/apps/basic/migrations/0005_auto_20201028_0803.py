# Generated by Django 3.0.7 on 2020-10-28 00:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0004_cutinfo_f_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportsinfo',
            name='date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='日期'),
        ),
        migrations.AlterField(
            model_name='basicinfo',
            name='variety',
            field=models.IntegerField(blank=True, choices=[(0, '湖羊'), (1, '小尾寒羊'), (2, '无角道赛特'), (3, '黑羊'), (4, '小尾4'), (5, '小尾5'), (6, '小尾6')], null=True, verbose_name='品种'),
        ),
    ]
