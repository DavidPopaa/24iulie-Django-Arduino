# Generated by Django 4.0.6 on 2022-07-22 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_delete_volume'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ModelDb',
            new_name='UserModel',
        ),
    ]
