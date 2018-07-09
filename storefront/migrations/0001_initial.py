# Generated by Django 2.0.7 on 2018-07-09 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='storeItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(default='NoName', max_length=200)),
                ('item_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('item_is_available', models.BooleanField(default=True)),
                ('item_description', models.CharField(default='None', max_length=500)),
                ('item_image', models.FileField(default='media', upload_to='')),
            ],
        ),
    ]
