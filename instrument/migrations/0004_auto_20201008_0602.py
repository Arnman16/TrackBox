# Generated by Django 3.0.7 on 2020-10-08 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instrument', '0003_instrument_starred'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timedata',
            old_name='time',
            new_name='datetime',
        ),
    ]
