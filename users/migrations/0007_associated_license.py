# Generated by Django 4.1.2 on 2022-12-22 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_company_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='associated',
            name='license',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
