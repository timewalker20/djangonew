# Generated by Django 3.2.15 on 2022-09-14 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cncapp', '0097_rename_transaction_id_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ManyToManyField(null=True, to='cncapp.Inventory'),
        ),
    ]
