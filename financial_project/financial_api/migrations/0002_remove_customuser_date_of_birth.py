# Generated by Django 4.2.2 on 2023-09-01 16:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("financial_api", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="date_of_birth",
        ),
    ]
