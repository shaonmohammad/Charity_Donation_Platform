# Generated by Django 4.2.3 on 2023-10-11 22:55

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogmodel",
            name="body",
            field=tinymce.models.HTMLField(),
        ),
    ]