# Generated by Django 3.2.16 on 2023-01-17 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cncapp', '0124_rename_channel_docdatashare_channelname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='docdatashare',
            old_name='channelname',
            new_name='channelName',
        ),
    ]