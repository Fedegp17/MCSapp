# Generated by Django 5.0.2 on 2024-03-23 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_endpoint', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='beatsperminute',
            options={'ordering': ['-created'], 'verbose_name': 'Pulsos por minuto', 'verbose_name_plural': 'Pulsos por minuto'},
        ),
    ]
