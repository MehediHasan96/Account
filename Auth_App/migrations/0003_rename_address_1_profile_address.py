# Generated by Django 3.2.6 on 2021-08-22 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Auth_App', '0002_remove_profile_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='address_1',
            new_name='address',
        ),
    ]
