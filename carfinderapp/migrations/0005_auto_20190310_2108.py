# Generated by Django 2.0.7 on 2019-03-10 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carfinderapp', '0004_auto_20190310_1838'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='manufacturer_id',
            new_name='manufacturer',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='model_id',
            new_name='model',
        ),
    ]
