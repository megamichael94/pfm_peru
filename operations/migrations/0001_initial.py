# Generated by Django 4.1.5 on 2023-03-13 02:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('id_number', models.CharField(blank=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='LineOfBusiness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('code', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='')),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('creation_datetime', models.DateTimeField(auto_now_add=True)),
                ('issue_date', models.DateField(default=django.utils.timezone.now)),
                ('total', models.FloatField()),
                ('taxes_percentage', models.IntegerField(default=10)),
                ('taxes', models.FloatField(blank=True, null=True)),
                ('total_without_taxes', models.FloatField(blank=True, null=True)),
                ('is_it_tax_deductible', models.BooleanField(default=True)),
                ('issuer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='operations.enterprise')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='')),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('creation_datetime', models.DateTimeField(auto_now_add=True)),
                ('issue_date', models.DateField(default=django.utils.timezone.now)),
                ('total', models.FloatField()),
                ('taxes_percentage', models.IntegerField(default=10)),
                ('taxes', models.FloatField(blank=True, null=True)),
                ('total_without_taxes', models.FloatField(blank=True, null=True)),
                ('is_it_tax_deductible', models.BooleanField(default=True)),
                ('issuer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='operations.enterprise')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='enterprise',
            name='line_of_business',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='operations.lineofbusiness'),
        ),
    ]