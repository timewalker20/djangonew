# Generated by Django 3.2.15 on 2022-08-24 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cncapp', '0071_alter_user_bloodgroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bloodgroup',
            field=models.CharField(default='B+', max_length=15),
        ),
    ]
