# Generated by Django 4.2.1 on 2023-05-29 20:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnel',
            name='started_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
