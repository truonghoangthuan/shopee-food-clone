# Generated by Django 3.2.8 on 2021-10-25 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_order', '0002_product_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customer_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customer_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customer_phone_number',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_stock_number',
            new_name='stock_number',
        ),
    ]
