# Generated by Django 5.0.7 on 2024-08-08 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='reg_d',
        ),
    ]
