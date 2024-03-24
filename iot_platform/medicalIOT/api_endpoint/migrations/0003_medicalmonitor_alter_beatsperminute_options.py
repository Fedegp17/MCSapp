# Generated by Django 5.0.2 on 2024-03-24 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_endpoint', '0002_alter_beatsperminute_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalMonitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40, verbose_name='Nombre')),
                ('heart_rate', models.FloatField(verbose_name='Ritmo cardiaco')),
                ('spo2', models.FloatField(verbose_name='Saturación de oxígeno')),
                ('respiracion', models.FloatField(verbose_name='Respiraciones por minuto')),
                ('presion_sistolica', models.FloatField(verbose_name='Presión sistólica')),
                ('presion_diastolica', models.FloatField(verbose_name='Presión diastolica')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Ultima modificación')),
            ],
            options={
                'verbose_name': 'Signos vitales',
                'verbose_name_plural': 'Signos vitales',
                'ordering': ['-created'],
            },
        ),
        migrations.AlterModelOptions(
            name='beatsperminute',
            options={'ordering': ['-created'], 'verbose_name': 'Pulsioximetro', 'verbose_name_plural': 'Pulsioximetro'},
        ),
    ]