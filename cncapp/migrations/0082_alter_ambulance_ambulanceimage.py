# Generated by Django 3.2.15 on 2022-08-28 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cncapp', '0081_alter_hospital_hospitalimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambulance',
            name='Ambulanceimage',
            field=models.ImageField(blank=True, null=True, upload_to='ambulance_pics'),
        ),
    ]
