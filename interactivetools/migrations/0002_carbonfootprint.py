# Generated by Django 5.0.6 on 2024-07-12 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interactivetools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarbonFootprint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miles_per_week', models.PositiveIntegerField()),
                ('carbon_footprint', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
