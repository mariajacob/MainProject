# Generated by Django 4.2.4 on 2023-09-14 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GHapp', '0026_patientprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientprofile',
            old_name='medications',
            new_name='medication_names',
        ),
    ]
