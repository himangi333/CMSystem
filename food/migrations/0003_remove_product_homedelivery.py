# Generated by Django 3.1.1 on 2020-10-11 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='homedelivery',
        ),
    ]
