# Generated by Django 4.2.1 on 2023-06-19 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_details',
            name='par_value',
            field=models.FloatField(default=3),
            preserve_default=False,
        ),
    ]
