# Generated by Django 5.1.4 on 2025-02-05 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0008_price_and_weight_sell_minimum_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='item_images'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='item_images'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='item_images'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='item_images'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='item_images'),
        ),
    ]
