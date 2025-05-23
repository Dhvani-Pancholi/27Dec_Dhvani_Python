# Generated by Django 5.2 on 2025-04-25 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=12)),
                ('city', models.CharField(max_length=100)),
                ('mobile', models.BigIntegerField()),
            ],
        ),
    ]
