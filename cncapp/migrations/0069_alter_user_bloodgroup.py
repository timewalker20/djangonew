# Generated by Django 3.2.15 on 2022-08-22 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cncapp', '0068_auto_20220822_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bloodgroup',
            field=models.CharField(choices=[('A-', 'A NEGATIVE'), ('AB-', 'AB NEGATIVE'), ('O-', 'O NEGATIVE'), ('O+', 'O POSITIVE'), ('B-', 'B NEGATIVE'), ('A+', 'A POSITIVE'), ('AB+', 'AB POSITIVE'), ('B+', 'B POSITIVE')], default='B+', max_length=15),
        ),
    ]
