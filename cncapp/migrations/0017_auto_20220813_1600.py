# Generated by Django 3.2.9 on 2022-08-13 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cncapp', '0016_alter_bloodgroup_bloodgroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodgroup',
            name='Bloodgroup',
            field=models.CharField(choices=[('A+', 'A POSITIVE'), ('AB+', 'AB POSITIVE'), ('O+', 'O POSITIVE'), ('B+', 'B POSITIVE'), ('AB-', 'AB NEGATIVE'), ('O-', 'O NEGATIVE'), ('B-', 'B NEGATIVE'), ('A-', 'A NEGATIVE')], default='B+', max_length=15),
        ),
        migrations.AlterField(
            model_name='gender',
            name='Gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='patient',
            name='contactno',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='pincode',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
