# Generated by Django 5.0.1 on 2024-01-18 00:39

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0004_user_products"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="products",
        ),
    ]
