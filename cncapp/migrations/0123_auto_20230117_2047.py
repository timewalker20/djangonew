# Generated by Django 3.2.16 on 2023-01-17 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cncapp', '0122_docdatashare_channel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ambulncedatashare',
            name='complete',
        ),
        migrations.AddField(
            model_name='docdatashare',
            name='current',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='docdatashare',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
