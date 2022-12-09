# Generated by Django 4.0.6 on 2022-08-16 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cncapp', '0035_alter_doctor_gender_alter_patient_bloodgroup_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='bloodgroup',
            field=models.CharField(choices=[('B+', 'B POSITIVE'), ('A-', 'A NEGATIVE'), ('AB+', 'AB POSITIVE'), ('AB-', 'AB NEGATIVE'), ('O+', 'O POSITIVE'), ('O-', 'O NEGATIVE'), ('B-', 'B NEGATIVE'), ('A+', 'A POSITIVE')], default='B+', max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='f', max_length=300),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='l', max_length=300),
        ),
        migrations.AlterField(
            model_name='user',
            name='usertype',
            field=models.CharField(choices=[('Driver', 'is-Driver'), ('Hospital', 'is_Hospital'), ('Patient', 'is_Patient'), ('Ambulance', 'is_Ambulance'), ('Doctor', 'is_Doctor'), ('Pharmacist', 'is_Pharmacist')], default='Doctor', max_length=50),
        ),
    ]
