# Generated by Django 5.0.3 on 2024-04-02 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='show',
            old_name='release_data',
            new_name='release_date',
        ),
    ]
