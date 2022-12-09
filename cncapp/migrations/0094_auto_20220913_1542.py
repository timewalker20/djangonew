# Generated by Django 3.2.15 on 2022-09-13 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cncapp', '0093_auto_20220913_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='ShippingAddress',
        ),
        migrations.RemoveField(
            model_name='order',
            name='orderitems',
        ),
        migrations.AddField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cncapp.order'),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cncapp.order'),
        ),
    ]
