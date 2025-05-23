# Generated by Django 5.2 on 2025-05-01 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorapp', '0003_rename_first_name_patientregistration_firstname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('appointdate', models.DateField()),
                ('drt', models.CharField(max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('message', models.TextField()),
            ],
        ),
    ]
