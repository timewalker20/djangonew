# Generated by Django 3.2.16 on 2023-01-17 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cncapp', '0121_tempory_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='docdatashare',
            name='channel',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]
