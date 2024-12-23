# Generated by Django 4.2.17 on 2024-12-23 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txref', models.CharField(max_length=20, unique=True)),
                ('weight_limit', models.FloatField(default=500)),
                ('battery_capacity', models.FloatField()),
                ('state', models.CharField(choices=[('IDLE', 'Idle'), ('LOADING', 'Loading'), ('LOADED', 'Loaded'), ('DELIVERING', 'Delivering'), ('DELIVERED', 'Delivered'), ('RETURNING', 'Returning')], default='IDLE', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('weight', models.FloatField()),
                ('code', models.CharField(default=1, max_length=100, unique=True)),
                ('box', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dispatch.box')),
            ],
        ),
    ]
