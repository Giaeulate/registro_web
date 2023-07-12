# Generated by Django 4.2.3 on 2023-07-11 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Municipio",
            fields=[
                (
                    "id",
                    models.CharField(max_length=150, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=150, verbose_name="Nombre")),
            ],
            options={
                "verbose_name": "Municipio",
                "verbose_name_plural": "Municipios",
                "ordering": ("id",),
            },
        ),
        migrations.CreateModel(
            name="Comunidad",
            fields=[
                (
                    "id",
                    models.CharField(max_length=150, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=150, verbose_name="Nombre")),
                (
                    "municipio",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.municipio"
                    ),
                ),
            ],
            options={
                "verbose_name": "Comunidad",
                "verbose_name_plural": "Comunidades",
                "ordering": ("id",),
            },
        ),
    ]