# Generated by Django 3.2.15 on 2022-08-16 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cncapp', '0043_auto_20220816_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='contact_no',
        ),
        migrations.AddField(
            model_name='user',
            name='phone_no',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctor',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='patient',
            name='bloodgroup',
            field=models.CharField(choices=[('A+', 'A POSITIVE'), ('A-', 'A NEGATIVE'), ('AB-', 'AB NEGATIVE'), ('O-', 'O NEGATIVE'), ('AB+', 'AB POSITIVE'), ('B-', 'B NEGATIVE'), ('O+', 'O POSITIVE'), ('B+', 'B POSITIVE')], default='B+', max_length=15),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='bloodgroup',
            field=models.CharField(choices=[('A+', 'A POSITIVE'), ('A-', 'A NEGATIVE'), ('AB-', 'AB NEGATIVE'), ('O-', 'O NEGATIVE'), ('AB+', 'AB POSITIVE'), ('B-', 'B NEGATIVE'), ('O+', 'O POSITIVE'), ('B+', 'B POSITIVE')], default='B+', max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='usertype',
            field=models.CharField(choices=[('Pharmacist', 'is_Pharmacist'), ('Doctor', 'is_Doctor'), ('Ambulance', 'is_Ambulance'), ('Patient', 'is_Patient'), ('Hospital', 'is_Hospital'), ('Driver', 'is-Driver')], default='Doctor', max_length=50),
        ),
    ]
