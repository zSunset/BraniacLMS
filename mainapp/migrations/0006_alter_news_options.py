# Generated by Django 3.2.16 on 2023-02-18 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0005_rename_cource_courseteachers_course"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="news",
            options={"ordering": ("-created",), "verbose_name": "News", "verbose_name_plural": "News"},
        ),
    ]