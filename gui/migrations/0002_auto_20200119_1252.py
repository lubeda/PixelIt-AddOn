# Generated by Django 3.0.2 on 2020-01-19 11:52

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('gui', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='template',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
        ),
    ]
