# Generated by Django 5.0.1 on 2024-01-30 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxorders', '0004_alter_taxorder_balance_alter_taxorder_consumed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxorder',
            name='contract_number',
            field=models.CharField(max_length=255),
        ),
    ]
