# Generated by Django 4.2.4 on 2023-09-14 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GHapp', '0023_remove_appointment_is_active_ashaworker_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ashaworker',
            name='date_of_birth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='ashaworker',
            name='date_of_join',
            field=models.DateField(),
        ),
    ]