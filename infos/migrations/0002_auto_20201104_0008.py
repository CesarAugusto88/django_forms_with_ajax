# Generated by Django 3.1.3 on 2020-11-04 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='descripton',
            new_name='description',
        ),
    ]
