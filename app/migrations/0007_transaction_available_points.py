# Generated by Django 3.2.13 on 2022-05-18 14:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_available_points_transaction_initial_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='available_points',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
