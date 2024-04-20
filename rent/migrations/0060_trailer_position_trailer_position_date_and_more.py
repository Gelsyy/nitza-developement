# Generated by Django 4.2.2 on 2024-04-20 13:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0059_alter_lesseedata_contact_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='trailer',
            name='position',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(8)]),
        ),
        migrations.AddField(
            model_name='trailer',
            name='position_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='trailer',
            name='position_note',
            field=models.TextField(null=True),
        ),
    ]
