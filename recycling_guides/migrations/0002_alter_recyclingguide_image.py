# Generated by Django 5.0.2 on 2024-07-25 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recycling_guides', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recyclingguide',
            name='image',
            field=models.ImageField(upload_to='static/images/recycling_guides/'),
        ),
    ]
