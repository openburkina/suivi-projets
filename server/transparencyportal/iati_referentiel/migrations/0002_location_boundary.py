# Generated by Django 4.1.5 on 2023-01-09 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("iati_referentiel", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="location",
            name="boundary",
            field=models.JSONField(blank=True, null=True),
        ),
    ]