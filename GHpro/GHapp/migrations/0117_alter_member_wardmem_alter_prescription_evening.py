# Generated by Django 4.2.4 on 2024-03-06 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GHapp', '0116_alter_member_wardmem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='wardmem',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='evening',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='evening',
            field=models.BooleanField(default=False),
        ),
    ]
