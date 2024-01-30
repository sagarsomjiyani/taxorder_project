# Generated by Django 5.0.1 on 2024-01-30 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxorders', '0005_alter_taxorder_contract_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxorder',
            name='fiscalyear',
            field=models.IntegerField(default=2023, max_length=4),
        ),
        migrations.AddField(
            model_name='taxorder',
            name='sectioncode',
            field=models.CharField(default='CP', max_length=3),
        ),
    ]
