# Generated by Django 4.2.4 on 2024-03-06 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GHapp', '0119_prescription_appointment_alter_prescription_morning'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='evening',
            field=models.BooleanField(default=False, null=True, blank=True),
        ),
    ]