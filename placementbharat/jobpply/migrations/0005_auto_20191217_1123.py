# Generated by Django 2.2 on 2019-12-17 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobpply', '0004_auto_20191217_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='address',
            field=models.CharField(blank=True, default='sample', max_length=100),
        ),
        migrations.AddField(
            model_name='info',
            name='emailid',
            field=models.CharField(blank=True, default='sample', max_length=50),
        ),
        migrations.AddField(
            model_name='info',
            name='number',
            field=models.CharField(blank=True, default='sample', max_length=15),
        ),
    ]
