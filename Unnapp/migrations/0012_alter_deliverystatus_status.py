# Generated by Django 5.0.4 on 2024-04-29 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Unnapp', '0011_deliverystatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliverystatus',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending')], default='Pending', max_length=50),
        ),
    ]