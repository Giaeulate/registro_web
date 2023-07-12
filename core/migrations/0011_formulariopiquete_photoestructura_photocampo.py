# Generated by Django 4.2.3 on 2023-07-12 07:06

import core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0010_alter_formularioencuesta_photo_ci_back_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="FormularioPiquete",
            fields=[
                (
                    "id",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=255)),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
                (
                    "comunidad",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.comunidad"
                    ),
                ),
            ],
            options={
                "verbose_name": "Formulario Piquete",
                "verbose_name_plural": "Formularios Piquete",
                "ordering": ("id",),
            },
        ),
        migrations.CreateModel(
            name="PhotoEstructura",
            fields=[
                (
                    "id",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                (
                    "url",
                    core.models.URLFieldExtended(blank=True, max_length=500, null=True),
                ),
                (
                    "form",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.formulariopiquete",
                    ),
                ),
            ],
            options={
                "verbose_name": "Photo Estructura",
                "verbose_name_plural": "Photos Estructuras",
                "ordering": ("id",),
            },
        ),
        migrations.CreateModel(
            name="PhotoCampo",
            fields=[
                (
                    "id",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                (
                    "url",
                    core.models.URLFieldExtended(blank=True, max_length=500, null=True),
                ),
                (
                    "form",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.formulariopiquete",
                    ),
                ),
            ],
            options={
                "verbose_name": "Photo Campo",
                "verbose_name_plural": "Photos Campo",
                "ordering": ("id",),
            },
        ),
    ]
