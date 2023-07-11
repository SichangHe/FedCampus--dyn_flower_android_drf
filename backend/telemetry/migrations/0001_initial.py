# Generated by Django 4.2.2 on 2023-06-26 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('train', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(auto_now=True)),
                ('tflite_model', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='training_sessions', to='train.tflitemodel')),
            ],
        ),
        migrations.CreateModel(
            name='FitInsTelemetryData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.IntegerField(editable=False)),
                ('start', models.DateTimeField(editable=False)),
                ('end', models.DateTimeField(editable=False)),
                ('session_id', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='fit_ins', to='telemetry.trainingsession')),
            ],
        ),
        migrations.CreateModel(
            name='EvaluateInsTelemetryData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.IntegerField(editable=False)),
                ('start', models.DateTimeField(editable=False)),
                ('end', models.DateTimeField(editable=False)),
                ('loss', models.FloatField(editable=False)),
                ('accuracy', models.FloatField(editable=False)),
                ('test_size', models.IntegerField(editable=False)),
                ('session_id', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='evaluate_ins', to='telemetry.trainingsession')),
            ],
        ),
    ]