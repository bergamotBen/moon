# These controllers create dictionaries which supply the context to the views
from .models import Advanced
from datetime import datetime
import math

import math

def moon_image_selector(days_to_new_moon):
    filestring = "moon_"
    if days_to_new_moon == 30:
        return filestring + "24.jpg"
    else:
        return (filestring + str(math.ceil((days_to_new_moon/29)*24)) + ".jpg")
    
def timestamp_to_hhmm(timestamp):
    converted_timestamp = datetime.fromtimestamp(timestamp)
    return f"{converted_timestamp.hour}:{converted_timestamp.minute}"

def timestamp_to_ddmm(timestamp):
    days = [(1, '1st'), (21, "21st"), (31, "31st"), (2, "2nd"), (22, "22nd", (3, "3rd"), (23, "23rd"))]   
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    converted_timestamp = datetime.fromtimestamp(timestamp)

    for day in days:
        ordinal = str()
        if day[0] == converted_timestamp.day:
            ordinal += day[1]
        else:
            ordinal += f"{converted_timestamp.day}th"

    return f"{ordinal} {months[converted_timestamp.month-1]}"

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