# Generated by Django 3.2.6 on 2021-11-12 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_order', '0002_customer_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='address',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='district',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='province',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='ward',
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='lattitude',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='longitude',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
