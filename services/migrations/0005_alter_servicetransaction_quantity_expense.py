# Generated by Django 4.1.2 on 2022-12-12 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_company_id'),
        ('utils', '0001_initial'),
        ('services', '0004_servicetransaction_delete_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicetransaction',
            name='quantity',
            field=models.FloatField(default=1),
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concept', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True)),
                ('cost', models.FloatField(blank=True)),
                ('associated', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.associated')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utils.order')),
            ],
        ),
    ]
