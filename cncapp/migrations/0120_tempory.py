# Generated by Django 3.2.16 on 2023-01-16 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cncapp', '0119_auto_20230116_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tempory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.CharField(max_length=13, unique=True)),
                ('otp', models.CharField(blank=True, max_length=6, null=True)),
            ],
        ),
    ]
