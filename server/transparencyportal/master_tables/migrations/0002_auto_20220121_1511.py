# Generated by Django 3.1.13 on 2022-01-21 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master_tables', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sector',
            name='end_year',
        ),
        migrations.RemoveField(
            model_name='sector',
            name='start_year',
        ),
    ]