# Generated by Django 3.2.13 on 2022-05-18 17:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_transaction_available_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='available_points',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='initial_points',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
