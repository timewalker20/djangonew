# Generated by Django 3.2.15 on 2022-12-17 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cncapp', '0110_auto_20221216_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='docdatashare',
            name='rtc',
            field=models.TextField(null=True),
        ),
    ]
