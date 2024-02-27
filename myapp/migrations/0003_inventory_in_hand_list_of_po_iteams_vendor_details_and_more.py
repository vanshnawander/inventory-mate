
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_product_details_par_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='inventory_in_hand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='list_of_po_iteams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_id', models.IntegerField()),
                ('product_name', models.CharField(max_length=50)),
                ('product_price', models.FloatField()),
                ('vendor_name', models.CharField(max_length=30)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(max_length=30)),
                ('user_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='vendor_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_id', models.IntegerField()),
                ('vendor_name', models.CharField(max_length=30)),
                ('vendor_phone', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='product_details',
            name='par_value',
        ),
        migrations.CreateModel(
            name='vendor_price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_price', models.FloatField()),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product_details')),
                ('vendor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.vendor_details')),
            ],
        ),
    ]
