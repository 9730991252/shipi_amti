# Generated by Django 5.1.4 on 2025-02-09 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Item',
            new_name='hotel_Item',
        ),
    ]
