# Generated by Django 5.0.1 on 2024-01-13 00:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("userAvatar", "0007_alter_useravatar_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="useravatar",
            name="user",
        ),
    ]
