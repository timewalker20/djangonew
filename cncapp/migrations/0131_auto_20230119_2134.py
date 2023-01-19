# Generated by Django 3.2.16 on 2023-01-19 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cncapp', '0130_docdatashare_start'),
    ]

    operations = [
        migrations.AddField(
            model_name='ambulance',
            name='latitude',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='ambulance',
            name='longitude',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='datashare',
            name='latitude',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='datashare',
            name='longitude',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='docdatashare',
            name='latitude',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='docdatashare',
            name='longitude',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='docdatashare',
            name='prescription_photo',
            field=models.ImageField(blank=True, null=True, upload_to='prescription_image'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='latitude',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='longitude',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='hospital',
            name='latitude',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='hospital',
            name='longitude',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='pathologist',
            name='latitude',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='pathologist',
            name='longitude',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='pathologydatashare',
            name='latitude',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='pathologydatashare',
            name='longitude',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='pharmacist',
            name='latitude',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='pharmacist',
            name='longitude',
            field=models.FloatField(default=0.0, null=True),
        ),
    ]
