# Generated by Django 4.1.2 on 2022-10-25 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_stock_profit'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock_price',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
