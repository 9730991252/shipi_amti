# Generated by Django 5.1.4 on 2025-02-09 09:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0002_customer_date_customer_district_customer_house_no_and_more'),
        ('owner', '0001_initial'),
        ('sunil', '0002_employee_delete_shope'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='owner.item')),
                ('price_and_weight', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='owner.price_and_weight')),
            ],
        ),
        migrations.CreateModel(
            name='Order_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0)),
                ('weight', models.IntegerField(default=0)),
                ('unit', models.CharField(blank=True, max_length=100, null=True)),
                ('qty', models.IntegerField(default=1)),
                ('order_filter', models.IntegerField(default=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('ordered_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('customer', models.ForeignKey(default=True, on_delete=django.db.models.deletion.PROTECT, to='customer.customer')),
                ('item', models.ForeignKey(default=True, on_delete=django.db.models.deletion.PROTECT, to='owner.item')),
            ],
        ),
        migrations.CreateModel(
            name='OrderMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel'), ('Pending', 'Pending')], default='Pending', max_length=50)),
                ('total_amount', models.FloatField(default=0, null=True)),
                ('order_filter', models.IntegerField(default=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('ordered_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('accepted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='sunil.employee')),
                ('customer', models.ForeignKey(default=True, on_delete=django.db.models.deletion.PROTECT, to='customer.customer')),
            ],
        ),
    ]
