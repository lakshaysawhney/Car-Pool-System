# Generated by Django 5.0.7 on 2024-07-23 19:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_point', models.CharField(default='Thapar University', max_length=255)),
                ('end_point', models.CharField(max_length=255)),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('transport_mode', models.CharField(max_length=50)),
                ('total_persons', models.IntegerField()),
                ('current_persons', models.IntegerField(default=1)),
                ('fare_per_head', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('description', models.CharField(blank=True, max_length=400, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_pools', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PoolMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_creator', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=10)),
                ('phone_number', models.CharField(max_length=10)),
                ('pool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='Pool.pool')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pools', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PoolRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('pool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='Pool.pool')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]