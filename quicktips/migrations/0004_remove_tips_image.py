# Generated by Django 5.0.6 on 2024-07-14 16:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("quicktips", "0003_rename_description_tips_description_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tips",
            name="image",
        ),
    ]