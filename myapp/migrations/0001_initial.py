# Generated by Django 4.2.2 on 2023-06-19 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.IntegerField()),
                ('product_name', models.CharField(max_length=50)),
                ('UOM', models.CharField(max_length=10)),
                ('tax_percentage', models.FloatField()),
                ('price', models.FloatField()),
                ('primary_vendor', models.CharField(max_length=30)),
                ('quantity_available', models.FloatField()),
            ],
        ),
    ]
