# Generated by Django 3.2.9 on 2022-08-09 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cncapp', '0008_alter_bloodgroup_bloodgroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodgroup',
            name='Bloodgroup',
            field=models.CharField(choices=[('A-', 'A NEGATIVE'), ('AB+', 'AB POSITIVE'), ('O+', 'O POSITIVE'), ('A+', 'A POSITIVE'), ('O-', 'O NEGATIVE'), ('B-', 'B NEGATIVE'), ('AB-', 'AB NEGATIVE'), ('B+', 'B POSITIVE')], default='B+', max_length=15),
        ),
        migrations.AlterField(
            model_name='gender',
            name='Gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
    ]
