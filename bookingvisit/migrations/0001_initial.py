# Generated by Django 3.2.4 on 2021-06-30 21:32

import datetime
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
            name='Beautician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=64)),
                ('workplace_number', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': '2 Kosmetyczki',
            },
        ),
        migrations.CreateModel(
            name='BServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=128)),
                ('time_service', models.IntegerField()),
                ('price_service', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': '4 Usługi kosmetyczne',
            },
        ),
        migrations.CreateModel(
            name='Client_Profil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(default='brak numeru', max_length=12)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '5 Użytkownicy',
            },
        ),
        migrations.CreateModel(
            name='Hairdresser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('surname', models.CharField(max_length=64)),
                ('workplace_number', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Fryzjera',
                'verbose_name_plural': '1 Fryzjerzy',
            },
        ),
        migrations.CreateModel(
            name='HServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=128)),
                ('time_service', models.IntegerField()),
                ('price_service', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': '3 Usługi fryzjerskie',
            },
        ),
        migrations.CreateModel(
            name='Reservation_Hairdresser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(null=True)),
                ('start_time', models.TimeField(default='08:00')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bookingvisit.client_profil')),
                ('employees', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingvisit.hairdresser')),
                ('services', models.ManyToManyField(to='bookingvisit.HServices')),
            ],
            options={
                'verbose_name_plural': '6 Rezerwacje do fryzjera',
            },
        ),
        migrations.CreateModel(
            name='Reservation_Beautician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(default=datetime.date.today)),
                ('start_time', models.TimeField(default='08:00')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingvisit.client_profil')),
                ('employees', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingvisit.beautician')),
                ('services', models.ManyToManyField(to='bookingvisit.BServices')),
            ],
            options={
                'verbose_name_plural': '7 Rezerwacje do kosmetyczki',
            },
        ),
        migrations.CreateModel(
            name='Opinions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=5)),
                ('opinion', models.TextField()),
                ('data', models.DateField(auto_now=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingvisit.client_profil')),
            ],
            options={
                'verbose_name_plural': '8 Opinie',
            },
        ),
        migrations.AddField(
            model_name='hairdresser',
            name='services',
            field=models.ManyToManyField(to='bookingvisit.HServices'),
        ),
        migrations.AddField(
            model_name='beautician',
            name='services',
            field=models.ManyToManyField(to='bookingvisit.BServices'),
        ),
    ]
