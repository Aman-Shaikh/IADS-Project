# Generated by Django 3.2.6 on 2024-08-05 20:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('request_services', '0003_alter_servicerequest_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
