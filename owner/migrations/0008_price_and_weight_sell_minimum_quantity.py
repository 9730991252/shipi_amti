# Generated by Django 5.1.4 on 2025-02-02 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0007_item_youtube_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='price_and_weight',
            name='sell_minimum_quantity',
            field=models.IntegerField(default=1),
        ),
    ]
