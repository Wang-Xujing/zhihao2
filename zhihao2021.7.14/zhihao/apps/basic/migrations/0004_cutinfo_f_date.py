# Generated by Django 3.0.7 on 2020-10-26 10:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0003_auto_20201008_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='cutinfo',
            name='f_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
    ]
