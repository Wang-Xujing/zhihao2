# Generated by Django 3.0.7 on 2021-04-11 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_breed', '0004_auto_20210108_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rutinfo',
            name='f_staff',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='创建人员'),
        ),
    ]