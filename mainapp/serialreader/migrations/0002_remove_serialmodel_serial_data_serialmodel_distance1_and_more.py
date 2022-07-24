# Generated by Django 4.0.6 on 2022-07-22 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serialreader', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serialmodel',
            name='serial_data',
        ),
        migrations.AddField(
            model_name='serialmodel',
            name='distance1',
            field=models.CharField(default='empty', max_length=1000),
        ),
        migrations.AddField(
            model_name='serialmodel',
            name='distance2',
            field=models.CharField(default='empty', max_length=1000),
        ),
        migrations.AddField(
            model_name='serialmodel',
            name='distance3',
            field=models.CharField(default='empty', max_length=1000),
        ),
        migrations.AddField(
            model_name='serialmodel',
            name='distance4',
            field=models.CharField(default='empty', max_length=1000),
        ),
    ]
