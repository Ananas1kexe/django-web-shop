# Generated by Django 5.2 on 2025-05-03 10:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="report",
            name="book",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="main.book",
            ),
        ),
    ]
