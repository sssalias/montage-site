# Generated by Django 5.0.7 on 2024-07-15 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addotionalservices',
            name='type',
        ),
    ]
