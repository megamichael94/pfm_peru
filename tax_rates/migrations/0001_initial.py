# Generated by Django 4.1.5 on 2023-03-08 17:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chunk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_value_range', models.FloatField()),
                ('max_value_range', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='UITValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=2022, unique=True, validators=[django.core.validators.MaxValueValidator(2100), django.core.validators.MinValueValidator(1994)])),
                ('value', models.FloatField()),
            ],
        ),
    ]