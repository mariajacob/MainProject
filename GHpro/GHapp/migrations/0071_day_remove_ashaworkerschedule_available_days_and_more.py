# Generated by Django 4.2.4 on 2023-09-28 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GHapp', '0070_ashaworkerschedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='ashaworkerschedule',
            name='available_days',
        ),
        migrations.AddField(
            model_name='ashaworkerschedule',
            name='available_days',
            field=models.ManyToManyField(blank=True, to='GHapp.day'),
        ),
    ]
