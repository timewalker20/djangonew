# Generated by Django 3.2.15 on 2022-08-24 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cncapp', '0072_alter_user_bloodgroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambulance',
            name='contact_no',
            field=models.CharField(default=0, max_length=13, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='ambulncedatashare',
            name='contactno',
            field=models.CharField(default=0, max_length=13),
        ),
        migrations.AlterField(
            model_name='datashare',
            name='contactno',
            field=models.CharField(default=0, max_length=13),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='contactno',
            field=models.CharField(default=0, max_length=13, unique=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='contact_no',
            field=models.CharField(default=0, max_length=13, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='contactno',
            field=models.CharField(default=0, max_length=13),
        ),
        migrations.AlterField(
            model_name='pharmacist',
            name='contact_no',
            field=models.CharField(default=0, max_length=13, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(default='Male', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_no',
            field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name='user',
            name='usertype',
            field=models.CharField(default=0, max_length=30),
        ),
    ]
