# Generated by Django 5.0 on 2024-04-20 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0007_rename_delivery_address_order_delivery_info"),
    ]

    operations = [
        migrations.CreateModel(
            name="DeliveryStatus",
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
                ("cart_info", models.TextField(blank=True)),
                ("status", models.CharField(max_length=50)),
                ("message", models.CharField(max_length=250)),
            ],
        ),
    ]
