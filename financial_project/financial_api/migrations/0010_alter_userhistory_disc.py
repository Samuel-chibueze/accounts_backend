# Generated by Django 4.2.2 on 2023-10-20 14:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("financial_api", "0009_userhistory_disc"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userhistory",
            name="disc",
            field=models.CharField(default="user deposit", max_length=100),
        ),
    ]