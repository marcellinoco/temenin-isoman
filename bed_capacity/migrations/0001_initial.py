# Generated by Django 3.2.8 on 2021-11-05 03:00

import bed_capacity.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wilayah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='RumahSakit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=40)),
                ('alamat', models.CharField(max_length=60)),
                ('kapasitas', models.IntegerField()),
                ('isi', models.IntegerField()),
                ('telp', models.CharField(max_length=25, validators=[bed_capacity.models.validate_telp])),
                ('kode_lokasi', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='bed_capacity.wilayah')),
            ],
        ),
        migrations.CreateModel(
            name='BedRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=40)),
                ('alamat', models.CharField(max_length=60)),
                ('gender', models.CharField(choices=[('L', 'Laki-laki'), ('P', 'Perempuan')], default='L', max_length=1)),
                ('umur', models.IntegerField()),
                ('telp', models.CharField(max_length=15, validators=[bed_capacity.models.validate_telp])),
                ('rs', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bed_capacity.rumahsakit')),
            ],
        ),
    ]