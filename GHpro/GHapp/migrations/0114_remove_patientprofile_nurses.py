# Generated by Django 4.2.4 on 2024-03-05 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GHapp', '0113_alter_member_wardmem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientprofile',
            name='nurses',
        ),
    ]
