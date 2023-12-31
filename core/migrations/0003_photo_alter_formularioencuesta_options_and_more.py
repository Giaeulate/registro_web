# Generated by Django 4.2.3 on 2023-07-12 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_formularioencuesta_alter_comunidad_municipio"),
    ]

    operations = [
        migrations.CreateModel(
            name="Photo",
            fields=[
                (
                    "id",
                    models.CharField(max_length=150, primary_key=True, serialize=False),
                ),
                ("url", models.URLField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Photo",
                "verbose_name_plural": "Photos",
                "ordering": ("id",),
            },
        ),
        migrations.AlterModelOptions(
            name="formularioencuesta",
            options={
                "ordering": ("id",),
                "verbose_name": "Formulario Encuesta",
                "verbose_name_plural": "Formularios Encuesta",
            },
        ),
        migrations.AlterField(
            model_name="formularioencuesta",
            name="photo_form",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="photo_form",
                to="core.photo",
            ),
        ),
        migrations.AlterField(
            model_name="formularioencuesta",
            name="photo_person",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="photo_person",
                to="core.photo",
            ),
        ),
    ]
