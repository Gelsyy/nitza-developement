# Generated by Django 4.1.5 on 2023-04-10 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0018_pendingpayment_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentcategory',
            name='chartColor',
            field=models.CharField(default='#8592a3', max_length=7),
        ),
        migrations.AddField(
            model_name='servicecategory',
            name='chartColor',
            field=models.CharField(default='#8592a3', max_length=7),
        ),
    ]
