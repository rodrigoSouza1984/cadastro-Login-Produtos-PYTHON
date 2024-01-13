# Generated by Django 5.0.1 on 2024-01-13 00:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
        ("userAvatar", "0008_remove_useravatar_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="userAvatar",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="userAvatar.useravatar",
            ),
        ),
    ]