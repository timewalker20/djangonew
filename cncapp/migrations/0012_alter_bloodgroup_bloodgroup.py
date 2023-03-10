# Generated by Django 3.2.9 on 2022-08-12 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cncapp', '0011_auto_20220810_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodgroup',
            name='Bloodgroup',
            field=models.CharField(choices=[('B-', 'B NEGATIVE'), ('O+', 'O POSITIVE'), ('A+', 'A POSITIVE'), ('A-', 'A NEGATIVE'), ('O-', 'O NEGATIVE'), ('B+', 'B POSITIVE'), ('AB-', 'AB NEGATIVE'), ('AB+', 'AB POSITIVE')], default='B+', max_length=15),
        ),
    ]
