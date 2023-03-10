# Generated by Django 3.2.15 on 2022-08-17 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cncapp', '0056_auto_20220817_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='patient',
            name='bloodgroup',
            field=models.CharField(choices=[('B+', 'B POSITIVE'), ('O+', 'O POSITIVE'), ('A-', 'A NEGATIVE'), ('AB+', 'AB POSITIVE'), ('B-', 'B NEGATIVE'), ('A+', 'A POSITIVE'), ('AB-', 'AB NEGATIVE'), ('O-', 'O NEGATIVE')], default='B+', max_length=15),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='bloodgroup',
            field=models.CharField(choices=[('B+', 'B POSITIVE'), ('O+', 'O POSITIVE'), ('A-', 'A NEGATIVE'), ('AB+', 'AB POSITIVE'), ('B-', 'B NEGATIVE'), ('A+', 'A POSITIVE'), ('AB-', 'AB NEGATIVE'), ('O-', 'O NEGATIVE')], default='B+', max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='usertype',
            field=models.CharField(choices=[('Hospital', 'is_Hospital'), ('Patient', 'is_Patient'), ('Pharmacist', 'is_Pharmacist'), ('Driver', 'is-Driver'), ('Ambulance', 'is_Ambulance'), ('Doctor', 'is_Doctor')], default='Doctor', max_length=50),
        ),
    ]
