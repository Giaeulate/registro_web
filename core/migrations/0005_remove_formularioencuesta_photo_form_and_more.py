# Generated by Django 4.2.3 on 2023-07-12 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_alter_formularioencuesta_photo_form_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="formularioencuesta", name="photo_form",),
        migrations.RemoveField(model_name="formularioencuesta", name="photo_person",),
    ]
