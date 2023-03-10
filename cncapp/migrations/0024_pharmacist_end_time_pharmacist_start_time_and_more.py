# Generated by Django 4.0.6 on 2022-08-14 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cncapp', '0023_doctor_desc_doctor_doctorimage_doctor_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pharmacist',
            name='end_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='pharmacist',
            name='start_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='bloodgroup',
            name='Bloodgroup',
            field=models.CharField(choices=[('O-', 'O NEGATIVE'), ('B+', 'B POSITIVE'), ('AB-', 'AB NEGATIVE'), ('AB+', 'AB POSITIVE'), ('B-', 'B NEGATIVE'), ('O+', 'O POSITIVE'), ('A+', 'A POSITIVE'), ('A-', 'A NEGATIVE')], default='B+', max_length=15),
        ),
        migrations.AlterField(
            model_name='gender',
            name='Gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
    ]
