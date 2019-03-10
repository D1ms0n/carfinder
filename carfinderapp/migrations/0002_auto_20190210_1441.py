# Generated by Django 2.0.7 on 2019-02-10 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carfinderapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarToSnoopRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Car to Snoop relation',
                'verbose_name_plural': 'Car to Snoop relations',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('manufacturer_name', models.CharField(max_length=256, primary_key=True, serialize=False, verbose_name='Manufacturer Name')),
            ],
            options={
                'verbose_name': 'Manufacturer Name',
                'verbose_name_plural': 'Manufacturer Names',
            },
        ),
        migrations.CreateModel(
            name='ManufacturerId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autoria_id', models.CharField(max_length=256, null=True, verbose_name='Autoria_Id')),
                ('rst_id', models.CharField(max_length=256, null=True, verbose_name='RST_Id')),
                ('name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manufacturer_ids', to='carfinderapp.Manufacturer')),
            ],
            options={
                'verbose_name': 'Manufacturer Id',
                'verbose_name_plural': 'Manufacturer Ids',
            },
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('model_name', models.CharField(max_length=256, primary_key=True, serialize=False, verbose_name='Model Name')),
                ('manufacturer_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='model_names', to='carfinderapp.Manufacturer')),
            ],
            options={
                'verbose_name': 'Model Name',
                'verbose_name_plural': 'Model Names',
            },
        ),
        migrations.CreateModel(
            name='ModelId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autoria_id', models.CharField(max_length=256, null=True, verbose_name='Autoria_Id')),
                ('rst_id', models.CharField(max_length=256, null=True, verbose_name='RST_Id')),
                ('model_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='model_ids', to='carfinderapp.Model')),
            ],
            options={
                'verbose_name': 'Model Id',
                'verbose_name_plural': 'Model Ids',
            },
        ),
        migrations.CreateModel(
            name='SnoopDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_min', models.IntegerField(blank=True, null=True, verbose_name='Year min')),
                ('year_max', models.IntegerField(blank=True, null=True, verbose_name='Year max')),
                ('mileage_min', models.IntegerField(blank=True, null=True, verbose_name='Mileage min')),
                ('mileage_max', models.IntegerField(blank=True, null=True, verbose_name='Mileage max')),
                ('manufacturer_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='snoops', to='carfinderapp.Manufacturer')),
                ('model_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='snoops', to='carfinderapp.Model')),
            ],
            options={
                'verbose_name': 'SnoopDetail',
                'verbose_name_plural': 'SnoopDetails',
            },
        ),
        migrations.RemoveField(
            model_name='car',
            name='manufacturer',
        ),
        migrations.RemoveField(
            model_name='car',
            name='model',
        ),
        migrations.RemoveField(
            model_name='car',
            name='snoop',
        ),
        migrations.RemoveField(
            model_name='snoop',
            name='manufacturer',
        ),
        migrations.RemoveField(
            model_name='snoop',
            name='mileage_max',
        ),
        migrations.RemoveField(
            model_name='snoop',
            name='mileage_min',
        ),
        migrations.RemoveField(
            model_name='snoop',
            name='model',
        ),
        migrations.RemoveField(
            model_name='snoop',
            name='year_max',
        ),
        migrations.RemoveField(
            model_name='snoop',
            name='year_min',
        ),
        migrations.AddField(
            model_name='car',
            name='url',
            field=models.CharField(max_length=256, null=True, verbose_name='URL'),
        ),
        migrations.AddField(
            model_name='snoopdetail',
            name='snoop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='details', to='carfinderapp.Snoop'),
        ),
        migrations.AddField(
            model_name='cartosnooprelation',
            name='car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relations', to='carfinderapp.Car'),
        ),
        migrations.AddField(
            model_name='cartosnooprelation',
            name='snoop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relations', to='carfinderapp.Snoop'),
        ),
        migrations.AddField(
            model_name='car',
            name='manufacturer_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='carfinderapp.Manufacturer'),
        ),
        migrations.AddField(
            model_name='car',
            name='model_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='carfinderapp.Model'),
        ),
    ]
