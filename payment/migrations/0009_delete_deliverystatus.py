# Generated by Django 5.0 on 2024-04-20 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0008_deliverystatus"),
    ]

    operations = [
        migrations.DeleteModel(
            name="DeliveryStatus",
        ),
    ]
