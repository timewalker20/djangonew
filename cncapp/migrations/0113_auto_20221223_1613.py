# Generated by Django 3.2.9 on 2022-12-23 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cncapp', '0112_auto_20221217_2021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pathologist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='0', max_length=300)),
                ('email', models.EmailField(max_length=300, unique=True)),
                ('desc', models.TextField(max_length=400, null=True)),
                ('services', models.TextField(max_length=400, null=True)),
                ('pathologistimage', models.ImageField(blank=True, null=True, upload_to='pathologist_pics')),
                ('contactno', models.CharField(default='0', max_length=13, unique=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(default='0', max_length=20)),
                ('pincode', models.CharField(default='0', max_length=6)),
                ('experience', models.CharField(max_length=20)),
                ('speciality', models.CharField(max_length=20)),
                ('gender', models.CharField(default='0', max_length=10)),
                ('amount', models.FloatField(default=0.0, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='ambulncedatashare',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='datashare',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='docdatashare',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='PathologyDatashare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='0', max_length=300)),
                ('email', models.EmailField(max_length=300)),
                ('contactno', models.CharField(default='0', max_length=13)),
                ('disease', models.TextField(max_length=300)),
                ('aadhaarno', models.CharField(default='0', max_length=12)),
                ('emergency', models.TextField(max_length=400, null=True)),
                ('gender', models.CharField(default='M', max_length=10)),
                ('bloodgroup', models.CharField(default='B+', max_length=15)),
                ('accept', models.BooleanField(default=False)),
                ('time', models.CharField(default='0', max_length=50)),
                ('prescription', models.TextField(null=True)),
                ('complete', models.BooleanField(default=False)),
                ('Doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cncapp.pathologist')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PathologyBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted', models.BooleanField(default=False)),
                ('booking_amount', models.CharField(max_length=25)),
                ('booking_payment_id', models.CharField(max_length=100)),
                ('isPaid', models.BooleanField(default=False)),
                ('date', models.DateField(default=0)),
                ('start_time', models.TimeField(default=0)),
                ('pathologist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cncapp.pathologist')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
