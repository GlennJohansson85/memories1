# Generated by Django 5.0.6 on 2024-05-23 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='is_client',
            new_name='is_staff',
        ),
    ]