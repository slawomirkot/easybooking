# Generated by Django 3.2.4 on 2021-07-02 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookingvisit', '0009_auto_20210702_0715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation_hairdresser',
            name='services',
        ),
        migrations.AddField(
            model_name='reservation_hairdresser',
            name='services',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bookingvisit.hservices', verbose_name='Usługa'),
            preserve_default=False,
        ),
    ]
