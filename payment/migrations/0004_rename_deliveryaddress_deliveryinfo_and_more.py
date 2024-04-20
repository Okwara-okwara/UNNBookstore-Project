# Generated by Django 5.0 on 2024-04-12 21:59

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0003_order_orderitem"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="DeliveryAddress",
            new_name="DeliveryInfo",
        ),
        migrations.AlterModelOptions(
            name="deliveryinfo",
            options={"verbose_name_plural": "Delivery Info"},
        ),
    ]