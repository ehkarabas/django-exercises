# Generated by Django 4.2.1 on 2023-05-23 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('flight_number', models.CharField(max_length=64)),
                ('airline', models.CharField(choices=[('THY', 'Turkish Airlines'), ('PEG', 'Pagasus Airlines'), ('HUS', 'Huseyin Airlines')], max_length=3)),
                ('departure', models.PositiveSmallIntegerField(choices=[(1, 'Adana'), (7, 'Antalya'), (34, 'Istanbul'), (35, 'Izmir'), (16, 'Bursa'), (10, 'Balikesir')])),
                ('departure_date', models.DateField()),
                ('arrival', models.PositiveSmallIntegerField(choices=[(1, 'Adana'), (7, 'Antalya'), (34, 'Istanbul'), (35, 'Izmir'), (16, 'Bursa'), (10, 'Balikesir')])),
                ('arrival_date', models.DateField()),
                ('created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('0', 'Prefer Not To Say')], default='0', max_length=1)),
                ('email', models.EmailField(max_length=254)),
                ('created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.flight')),
                ('passenger', models.ManyToManyField(to='flight.passenger')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]