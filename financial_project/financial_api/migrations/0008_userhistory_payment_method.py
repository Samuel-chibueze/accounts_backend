# Generated by Django 4.2.2 on 2023-10-18 10:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("financial_api", "0007_remove_cryptomodel_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="userhistory",
            name="payment_method",
            field=models.CharField(default="2023-10-18", max_length=20),
            preserve_default=False,
        ),
    ]
