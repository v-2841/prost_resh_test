# Generated by Django 4.2.4 on 2023-11-29 10:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("items", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="item",
            options={
                "ordering": ["name"],
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
            },
        ),
    ]
