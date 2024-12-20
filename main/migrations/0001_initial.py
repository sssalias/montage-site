# Generated by Django 5.0.7 on 2024-07-15 16:48

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ServicesTypes',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LightService',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('radius', models.IntegerField()),
                ('price', models.FloatField(default=0)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.productstype')),
            ],
        ),
        migrations.CreateModel(
            name='HardService',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('radius', models.IntegerField()),
                ('price', models.FloatField(default=0)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.productstype')),
            ],
        ),
        migrations.CreateModel(
            name='FullLightService',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('radius', models.IntegerField()),
                ('price', models.FloatField(default=0)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.productstype')),
            ],
        ),
        migrations.CreateModel(
            name='FullHardService',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('radius', models.IntegerField()),
                ('price', models.FloatField(default=0)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.productstype')),
            ],
        ),
        migrations.CreateModel(
            name='AddotionalServices',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('price', models.FloatField(default=0)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.productstype')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('radius', models.IntegerField()),
                ('type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.servicestypes')),
            ],
        ),
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('service', models.TextField()),
                ('serivce_type', models.TextField()),
                ('bio', models.TextField()),
                ('radius', models.IntegerField()),
                ('phone', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.services')),
                ('type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.servicestypes')),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('radius', models.IntegerField()),
                ('price', models.FloatField(default=0)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.productstype')),
            ],
        ),
    ]
