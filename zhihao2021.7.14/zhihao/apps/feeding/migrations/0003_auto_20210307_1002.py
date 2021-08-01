# Generated by Django 3.0.7 on 2021-03-07 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeding', '0002_feedhouseinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedhouseinfo',
            name='growing',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='生长期'),
        ),
        migrations.AlterField(
            model_name='feedhouseinfo',
            name='n_diagnosis',
            field=models.BooleanField(blank=True, null=True, verbose_name='营养诊断'),
        ),
        migrations.AlterField(
            model_name='feedhouseinfo',
            name='n_requirements',
            field=models.TextField(blank=True, null=True, verbose_name='营养需求'),
        ),
        migrations.AlterField(
            model_name='feedhouseinfo',
            name='notes',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='备注'),
        ),
    ]
