# Generated by Django 4.2.2 on 2023-06-13 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='started_date',
            new_name='start_date',
        ),
    ]