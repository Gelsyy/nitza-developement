# Generated by Django 4.1.2 on 2022-10-14 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_product_quantity_alter_product_quantity_min_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associated',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='associated',
            name='note',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='inventorylocations',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='note',
            field=models.TextField(blank=True),
        ),
    ]
