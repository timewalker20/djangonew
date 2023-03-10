# Generated by Django 4.0.6 on 2022-08-16 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cncapp', '0038_remove_user_pincode_alter_doctor_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='bloodgroup',
            field=models.CharField(choices=[('O+', 'O POSITIVE'), ('O-', 'O NEGATIVE'), ('A-', 'A NEGATIVE'), ('B-', 'B NEGATIVE'), ('A+', 'A POSITIVE'), ('AB-', 'AB NEGATIVE'), ('B+', 'B POSITIVE'), ('AB+', 'AB POSITIVE')], default='B+', max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='bloodgroup',
            field=models.CharField(choices=[('O+', 'O POSITIVE'), ('O-', 'O NEGATIVE'), ('A-', 'A NEGATIVE'), ('B-', 'B NEGATIVE'), ('A+', 'A POSITIVE'), ('AB-', 'AB NEGATIVE'), ('B+', 'B POSITIVE'), ('AB+', 'AB POSITIVE')], default='B+', max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='contact_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='usertype',
            field=models.CharField(choices=[('Pharmacist', 'is_Pharmacist'), ('Doctor', 'is_Doctor'), ('Hospital', 'is_Hospital'), ('Driver', 'is-Driver'), ('Ambulance', 'is_Ambulance'), ('Patient', 'is_Patient')], default='Doctor', max_length=50),
        ),
    ]
