# Generated by Django 3.2.15 on 2022-09-13 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cncapp', '0094_auto_20220913_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='Pharmacist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cncapp.pharmacist'),
        ),
    ]
