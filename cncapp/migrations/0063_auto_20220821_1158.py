# Generated by Django 3.2.15 on 2022-08-21 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cncapp', '0062_auto_20220820_2246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospitaldoctor',
            name='user',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='pharma',
        ),
        migrations.AddField(
            model_name='hospital',
            name='hospitalimage',
            field=models.ImageField(blank=True, upload_to='hospital_pics'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='gender',
            field=models.CharField(default='M', max_length=10),
        ),
        migrations.AlterField(
            model_name='patient',
            name='bloodgroup',
            field=models.CharField(choices=[('O-', 'O NEGATIVE'), ('B+', 'B POSITIVE'), ('A+', 'A POSITIVE'), ('O+', 'O POSITIVE'), ('AB-', 'AB NEGATIVE'), ('A-', 'A NEGATIVE'), ('B-', 'B NEGATIVE'), ('AB+', 'AB POSITIVE')], default='B+', max_length=15),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], default='M', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='bloodgroup',
            field=models.CharField(choices=[('O-', 'O NEGATIVE'), ('B+', 'B POSITIVE'), ('A+', 'A POSITIVE'), ('O+', 'O POSITIVE'), ('AB-', 'AB NEGATIVE'), ('A-', 'A NEGATIVE'), ('B-', 'B NEGATIVE'), ('AB+', 'AB POSITIVE')], default='B+', max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(default='Patient', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='usertype',
            field=models.IntegerField(),
        ),
    ]
