# Generated by Django 4.2.2 on 2023-07-29 03:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("telemetry", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="evaluateinstelemetrydata",
            name="device_id",
            field=models.BigIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name="evaluateinstelemetrydata",
            name="test_size",
            field=models.BigIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name="fitinstelemetrydata",
            name="device_id",
            field=models.BigIntegerField(editable=False),
        ),
    ]
