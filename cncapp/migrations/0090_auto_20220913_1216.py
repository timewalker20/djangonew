# Generated by Django 3.2.15 on 2022-09-13 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cncapp', '0089_rename_customer_order_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='customer',
            new_name='user',
        ),
        migrations.AddField(
            model_name='order',
            name='shop_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cncapp.pharmacist'),
        ),
    ]
