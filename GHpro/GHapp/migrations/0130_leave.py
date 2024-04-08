# Generated by Django 4.2.4 on 2024-03-25 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GHapp', '0129_alter_prescription_model_evening_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_type', models.CharField(choices=[('Sick Leave', 'Sick Leave'), ('Vacation', 'Vacation'), ('Personal Leave', 'Personal Leave'), ('Other', 'Other')], max_length=20)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('reason', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, default='Pending', max_length=20, null=True)),
                ('asha_member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GHapp.ashaworker')),
                ('mem_member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GHapp.member')),
                ('nurse_member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GHapp.nurse')),
            ],
        ),
    ]