# Generated by Django 3.2.16 on 2023-01-16 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cncapp', '0118_auto_20230116_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='videocall',
        ),
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.CharField(default='0', max_length=11),
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
