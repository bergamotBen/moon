# These controllers create dictionaries which supply the context to the views
from .models import Advanced


def create_basic_dict(id):
    basic_context = dict()
    request = Advanced.objects.get(id=id)
    basic_context["timestamp"] = request.timestamp
    basic_context["sunrise_timestamp"] = request.sun_sunrise_timestamp
    basic_context["sunset_timestamp"] = request.sun_sunset_timestamp
    basic_context["moon_phase"] = request.moon_phase_name
    basic_context["moon_emoji"] = request.moon_phase_emoji
    basic_context["moonrise_timestamp"] = request.moon_moonrise_timestamp
    basic_context["moonset_timestamp"] = request.moon_moonset_timestamp
    basic_context["next_full_moon"] = request.moon_moon_phase_full_moon_next_datestamp
    basic_context["latitude"] = request.location_latitude
    basic_context["longitude"] = request.location_longitude

    return basic_context

def create_sun_dict(id):
    sun_context = dict()
    request = Advanced.objects.get(id=id)
    sun_context["timestamp"] = request.timestamp
    sun_context["sunrise_timestamp"] = request.sun_sunrise_timestamp
    sun_context["sunset_timestamp"] = request.sun_sunset_timestamp
    sun_context["day_length"] = request.sun_day_length
    sun_context["sun_azimuth"] = request.sun_azimuth
    sun_context["latitude"] = request.location_latitude
    sun_context["longitude"] = request.location_longitude

    return sun_context

def create_moon_dict(id):
    moon_context = dict()
    request = Advanced.objects.get(id=id)

    moon_context["timestamp"] = request.timestamp
    moon_context["moonrise"] = request.moon_moonrise_timestamp
    moon_context["moonset"] = request.moon_moonset_timestamp
    moon_context["phase_name"] = request.moon_phase_name
    moon_context["phase_stage"] = request.moon_phase_stage
    moon_context["phase_age"] = request.moon_phase_age_days
    moon_context["emoji"] = request.moon_phase_emoji
    moon_context["next_full_moon"] = request.moon_moon_phase_full_moon_next_datestamp
    moon_context["azimuth"] = request.moon_moon_azimuth
    moon_context["latitude"] = request.location_latitude
    moon_context["longitude"] = request.location_longitude

    return moon_context


def create_eclipses_dict(id):
    pass