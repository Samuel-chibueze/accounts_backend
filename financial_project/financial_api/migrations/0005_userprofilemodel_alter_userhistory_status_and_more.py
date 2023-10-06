# Generated by Django 4.2.2 on 2023-09-18 10:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("financial_api", "0004_alter_customuser_phonenumber"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfileModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Current_balance", models.FloatField(default=0.0)),
                ("Account_balance", models.FloatField(default=0.0)),
                ("Savings_balance", models.FloatField(default=0.0)),
                ("Investment", models.FloatField(default=0.0)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="userhistory",
            name="status",
            field=models.CharField(
                choices=[
                    ("Successful", "Successful"),
                    ("Pending", "Pending"),
                    ("Cancelled", "Cancelled"),
                ],
                default="Pending",
                max_length=11,
            ),
        ),
        migrations.DeleteModel(
            name="UserAccountModel",
        ),
    ]
