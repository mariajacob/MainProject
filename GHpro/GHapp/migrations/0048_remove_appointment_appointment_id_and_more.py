# Generated by Django 4.2.4 on 2023-09-19 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GHapp', '0047_appointment_appointment_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='appointment_id',
        ),
        migrations.AddField(
            model_name='appointment',
            name='is_approve',
            field=models.BooleanField(default=False),
        ),
    ]
