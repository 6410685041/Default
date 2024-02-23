# Generated by Django 5.0.2 on 2024-02-23 13:26

import location_field.models.plain
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "location",
                    location_field.models.plain.PlainLocationField(max_length=63),
                ),
                ("speed", models.FloatField()),
                ("color", models.TextField()),
                ("license_plate", models.TextField()),
                ("brand", models.TextField()),
                ("model", models.TextField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Motorbike",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "location",
                    location_field.models.plain.PlainLocationField(max_length=63),
                ),
                ("speed", models.FloatField()),
                ("color", models.TextField()),
                ("license_plate", models.TextField()),
                ("brand", models.TextField()),
                ("model", models.TextField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Truck",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "location",
                    location_field.models.plain.PlainLocationField(max_length=63),
                ),
                ("speed", models.FloatField()),
                ("color", models.TextField()),
                ("license_plate", models.TextField()),
                ("brand", models.TextField()),
                ("model", models.TextField()),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
