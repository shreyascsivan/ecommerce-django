# Generated by Django 4.2.3 on 2023-07-16 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='discount_price',
            new_name='mrp',
        ),
    ]
