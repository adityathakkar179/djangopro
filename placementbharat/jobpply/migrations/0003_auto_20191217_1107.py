# Generated by Django 2.2 on 2019-12-17 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobpply', '0002_info_card2head'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='card3head',
            field=models.CharField(blank=True, default='sample', max_length=50),
        ),
        migrations.AddField(
            model_name='info',
            name='card4head',
            field=models.CharField(blank=True, default='sample', max_length=50),
        ),
    ]
