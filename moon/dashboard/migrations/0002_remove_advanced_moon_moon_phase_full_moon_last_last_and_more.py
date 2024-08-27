# Generated by Django 5.1 on 2024-08-27 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advanced',
            name='moon_moon_phase_full_moon_last_last',
        ),
        migrations.RemoveField(
            model_name='advanced',
            name='moon_moon_phase_full_moon_last_type',
        ),
        migrations.RemoveField(
            model_name='advanced',
            name='moon_moon_phase_full_moon_next_next',
        ),
        migrations.RemoveField(
            model_name='advanced',
            name='moon_moon_phase_full_moon_next_type',
        ),
        migrations.RemoveField(
            model_name='advanced',
            name='moon_moon_phase_new_moon_last',
        ),
        migrations.RemoveField(
            model_name='advanced',
            name='moon_moon_phase_new_moon_next',
        ),
        migrations.RemoveField(
            model_name='advanced',
            name='moon_moon_phase_new_moon_next_timestamp',
        ),
        migrations.RemoveField(
            model_name='advanced',
            name='moon_moon_phase_new_moon_type',
        ),
        migrations.RemoveField(
            model_name='advanced',
            name='moon_moonrise_type',
        ),
        migrations.RemoveField(
            model_name='advanced',
            name='moon_next_lunar_eclipse_type',
        ),
        migrations.RemoveField(
            model_name='advanced',
            name='moon_phase_zodiac_type',
        ),
        migrations.RemoveField(
            model_name='advanced',
            name='moon_type',
        ),
        migrations.AddField(
            model_name='advanced',
            name='moon_phase_lunar_cycle',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='advanced',
            name='location_latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='advanced',
            name='location_longitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='advanced',
            name='moon_moon_altitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='advanced',
            name='moon_moon_azimuth',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='advanced',
            name='moon_moon_distance',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='advanced',
            name='moon_moon_parallactic_angle',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='advanced',
            name='moon_moon_phase_full_moon_last_days_ago',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='advanced',
            name='moon_moon_phase_full_moon_last_timestamp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='advanced',
            name='moon_moon_phase_full_moon_next_days_ahead',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='advanced',
            name='moon_moon_phase_full_moon_next_timestamp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='advanced',
            name='moon_moon_phase_new_moon_last_days_ago',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='advanced',
            name='moon_moon_phase_new_moon_last_timestamp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='advanced',
            name='moon_moon_phase_new_moon_next_days_ahead',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='advanced',
            name='moon_moonrise_timestamp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='advanced',
            name='moon_moonset_timestamp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='advanced',
            name='moon_next_lunar_eclipse_timestamp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='advanced',
            name='moon_phase_age_days',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='advanced',
            name='moon_phase_emoji',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='advanced',
            name='moon_phase_illumination',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='advanced',
            name='moon_phase_type',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='advanced',
            name='sun_altitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='advanced',
            name='sun_azimuth',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='advanced',
            name='sun_distance',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='advanced',
            name='sun_next_solar_eclipse_timestamp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='advanced',
            name='sun_sunrise_timestamp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='advanced',
            name='sun_sunset_timestamp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='advanced',
            name='timestamp',
            field=models.IntegerField(),
        ),
    ]
