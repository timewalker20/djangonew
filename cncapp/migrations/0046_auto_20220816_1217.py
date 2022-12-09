# Generated by Django 3.2.15 on 2022-08-16 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cncapp', '0045_auto_20220816_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambulance',
            name='areacode',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='pincode',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='pincode',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patient',
            name='bloodgroup',
            field=models.CharField(choices=[('O+', 'O POSITIVE'), ('A-', 'A NEGATIVE'), ('O-', 'O NEGATIVE'), ('A+', 'A POSITIVE'), ('B+', 'B POSITIVE'), ('B-', 'B NEGATIVE'), ('AB+', 'AB POSITIVE'), ('AB-', 'AB NEGATIVE')], default='B+', max_length=15),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='patient',
            name='pincode',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='pharmacist',
            name='pincode',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='bloodgroup',
            field=models.CharField(choices=[('O+', 'O POSITIVE'), ('A-', 'A NEGATIVE'), ('O-', 'O NEGATIVE'), ('A+', 'A POSITIVE'), ('B+', 'B POSITIVE'), ('B-', 'B NEGATIVE'), ('AB+', 'AB POSITIVE'), ('AB-', 'AB NEGATIVE')], default='B+', max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='usertype',
            field=models.CharField(choices=[('Ambulance', 'is_Ambulance'), ('Driver', 'is-Driver'), ('Pharmacist', 'is_Pharmacist'), ('Hospital', 'is_Hospital'), ('Patient', 'is_Patient'), ('Doctor', 'is_Doctor')], default='Doctor', max_length=50),
        ),
    ]
