# Generated by Django 4.2.2 on 2023-10-18 01:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("financial_api", "0006_alter_userhistory_transaction_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cryptomodel",
            name="user",
        ),
    ]
