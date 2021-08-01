# Generated by Django 3.0.7 on 2021-01-08 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_breed', '0003_export_breed'),
    ]

    operations = [
        migrations.AddField(
            model_name='breedinginfo',
            name='mat_period',
            field=models.IntegerField(blank=True, null=True, verbose_name='配种情期(天)'),
        ),
        migrations.AddField(
            model_name='breedinginfo',
            name='single_ok',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='单次配种成功率(%)'),
        ),
    ]
