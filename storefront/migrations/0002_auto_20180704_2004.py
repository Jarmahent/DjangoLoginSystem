# Generated by Django 2.0.1 on 2018-07-05 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storefront', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store_item',
            name='id',
        ),
        migrations.AlterField(
            model_name='store_item',
            name='item_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]