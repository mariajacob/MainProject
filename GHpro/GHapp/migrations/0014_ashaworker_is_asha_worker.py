# Generated by Django 4.2.4 on 2023-09-12 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GHapp', '0013_remove_ashaworker_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ashaworker',
            name='is_asha_worker',
            field=models.BooleanField(default=True),
        ),
    ]