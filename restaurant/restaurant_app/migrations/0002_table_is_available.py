# Generated by Django 5.2.3 on 2025-06-27 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
