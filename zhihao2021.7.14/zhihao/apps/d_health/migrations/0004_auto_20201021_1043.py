# Generated by Django 3.0.7 on 2020-10-21 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('d_health', '0003_auto_20201021_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quarantineinfo',
            name='detection_mode',
            field=models.IntegerField(blank=True, choices=[(0, '尿检'), (1, '血检')], null=True, verbose_name='检测方式'),
        ),
    ]
