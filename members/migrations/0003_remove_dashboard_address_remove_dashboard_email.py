# Generated by Django 4.2.6 on 2024-02-26 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_dashboard_address_dashboard_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashboard',
            name='address',
        ),
        migrations.RemoveField(
            model_name='dashboard',
            name='email',
        ),
    ]