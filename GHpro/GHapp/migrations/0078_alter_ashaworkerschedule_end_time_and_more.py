# Generated by Django 4.2.4 on 2023-09-29 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GHapp', '0077_remove_ashaworkerschedule_ashaworker_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ashaworkerschedule',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ashaworkerschedule',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]