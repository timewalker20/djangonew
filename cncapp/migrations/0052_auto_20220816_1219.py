# Generated by Django 3.2.15 on 2022-08-16 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cncapp', '0051_auto_20220816_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='bloodgroup',
            field=models.CharField(choices=[('O-', 'O NEGATIVE'), ('B-', 'B NEGATIVE'), ('AB+', 'AB POSITIVE'), ('AB-', 'AB NEGATIVE'), ('B+', 'B POSITIVE'), ('O+', 'O POSITIVE'), ('A-', 'A NEGATIVE'), ('A+', 'A POSITIVE')], default='B+', max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='bloodgroup',
            field=models.CharField(choices=[('O-', 'O NEGATIVE'), ('B-', 'B NEGATIVE'), ('AB+', 'AB POSITIVE'), ('AB-', 'AB NEGATIVE'), ('B+', 'B POSITIVE'), ('O+', 'O POSITIVE'), ('A-', 'A NEGATIVE'), ('A+', 'A POSITIVE')], default='B+', max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='usertype',
            field=models.CharField(choices=[('Doctor', 'is_Doctor'), ('Pharmacist', 'is_Pharmacist'), ('Driver', 'is-Driver'), ('Hospital', 'is_Hospital'), ('Ambulance', 'is_Ambulance'), ('Patient', 'is_Patient')], default='Doctor', max_length=50),
        ),
    ]
