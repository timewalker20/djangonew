# Generated by Django 3.2.15 on 2022-08-22 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cncapp', '0067_auto_20220822_1831'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DatashareAmbulnce',
            new_name='AmbulnceDatashare',
        ),
        migrations.AlterField(
            model_name='user',
            name='bloodgroup',
            field=models.CharField(choices=[('A+', 'A POSITIVE'), ('O-', 'O NEGATIVE'), ('O+', 'O POSITIVE'), ('AB-', 'AB NEGATIVE'), ('B-', 'B NEGATIVE'), ('AB+', 'AB POSITIVE'), ('B+', 'B POSITIVE'), ('A-', 'A NEGATIVE')], default='B+', max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='usertype',
            field=models.IntegerField(null=True),
        ),
    ]
