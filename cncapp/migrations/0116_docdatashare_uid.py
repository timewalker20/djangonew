# Generated by Django 3.2.16 on 2023-01-13 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cncapp', '0115_rename_time_docdatashare_timeofshare'),
    ]

    operations = [
        migrations.AddField(
            model_name='docdatashare',
            name='uid',
            field=models.IntegerField(default=0),
        ),
    ]