from django.http import HttpResponse
from . import views
from .models import Advanced
from django.shortcuts import render
from .controllers import create_sun_dict, create_moon_dict, moon_image_selector
import requests
from django.http import JsonResponse
from dotenv import load_dotenv
import os
import json

def index(request):
    context = dict()
    context["count"] = Advanced.objects.count()
    return render(request, 'dashboard/dashboard.html', context)

def sun(request, advanced_id):
    context = create_sun_dict(advanced_id)
    context["count"] = Advanced.objects.count()
    return render(request, "dashboard/sun.html", context)

def moon(request, advanced_id):
    context = create_moon_dict(advanced_id)
    context["count"] = Advanced.objects.count()

    return render(request, "dashboard/moon.html", context)

def eclipses(request, advanced_id):
    advanced = Advanced.objects.get(id=advanced_id)
    context = {"advanced" : advanced.moon_phase_name,
               "moon_age": advanced.moon_phase_age_days}
    context["count"] = Advanced.objects.count()
    
    return render(request, "dashboard/eclipses.html", context)

def update(request):
    api_key = os.environ.get('API_KEY')
    print(api_key[8::])
    # turn this into a cron job
    def create_record():
        url = "https://moon-phase.p.rapidapi.com/advanced"

        querystring = {"lat":"51.4583","lon":"-2.5591"}

        headers = {
            "x-rapidapi-key": api_key[8::],
            "x-rapidapi-host": "moon-phase.p.rapidapi.com"
    }

        response_str = requests.get(url, headers=headers, params=querystring)

        response = response_str.json()

        new_record = Advanced(timestamp = response["timestamp"],
            datestamp = response["datestamp"],
            sun_sunrise_timestamp = response["sun"]["sunrise"],
            sun_sunset_timestamp = response["sun"]["sunset"],
            sun_solar_noon =response["sun"]["solar_noon"],
            sun_day_length = response["sun"]["day_length"],
            sun_altitude = response["sun"]["sun_altitude"],
            sun_distance = response["sun"]["sun_distance"],
            sun_azimuth = response["sun"]["sun_azimuth"],
            sun_next_solar_eclipse_timestamp = response["sun"]["next_solar_eclipse"]["timestamp"],
            sun_next_solar_eclipse_datestamp = response["sun"]["next_solar_eclipse"]["datestamp"],
            sun_next_solar_eclipse_type = response["sun"]["next_solar_eclipse"]["type"],
            sun_next_solar_eclipse_visibility_regions = response["sun"]["next_solar_eclipse"]["visibility_regions"],
            moon_phase_type = response["moon"]["phase"],
            moon_phase_name = response["moon"]["phase_name"],
            moon_phase_stage = response["moon"]["stage"],
            moon_phase_illumination = response["moon"]["illumination"],
            moon_phase_age_days = response["moon"]["age_days"],
            moon_phase_lunar_cycle = response["moon"]["lunar_cycle"],
            moon_phase_emoji = response["moon"]["emoji"],
            moon_phase_zodiac_sun_sign = response["moon"]["zodiac"]["sun_sign"],
            moon_phase_zodiac_moon_sign = response["moon"]["zodiac"]["moon_sign"],
            moon_moonrise_timestamp = response["moon"]["moonrise"],
            moon_moonset_timestamp =response["moon"]["moonset"],
            moon_moon_altitude = response["moon"]["moon_altitude"],
            moon_moon_distance = response["moon"]["moon_distance"],
            moon_moon_azimuth = response["moon"]["moon_azimuth"],
            moon_moon_parallactic_angle = response["moon"]["moon_parallactic_angle"],
            moon_next_lunar_eclipse_timestamp = response["moon"]["next_lunar_eclipse"]["timestamp"],
            moon_next_lunar_eclipse_datestamp = response["moon"]["next_lunar_eclipse"]["datestamp"],
            moon_moon_phase_type = response["moon"]["next_lunar_eclipse"]["type"],
            moon_next_lunar_eclipse_visibility_regions = response["moon"]["next_lunar_eclipse"]["visibility_regions"],
            moon_moon_phase_new_moon_last_timestamp = response["moon_phases"]["new_moon"]["last"]["timestamp"],
            moon_moon_phase_new_moon_last_datestamp = response["moon_phases"]["new_moon"]["last"]["datestamp"],
            moon_moon_phase_new_moon_last_days_ago = response["moon_phases"]["new_moon"]["last"]["days_ago"],
            #moon_moon_phase_new_moon_next_timestamp = response["moon_phases"]["new_moon"]["next"]["timestamp"],
            moon_moon_phase_new_moon_next_datestamp = response["moon_phases"]["new_moon"]["next"]["datestamp"],
            moon_moon_phase_new_moon_next_days_ahead = response["moon_phases"]["new_moon"]["next"]["days_ahead"],
            moon_moon_phase_full_moon_last_timestamp = response["moon_phases"]["full_moon"]["last"]["timestamp"],
            moon_moon_phase_full_moon_last_datestamp = response["moon_phases"]["full_moon"]["last"]["datestamp"],
            moon_moon_phase_full_moon_last_days_ago = response["moon_phases"]["full_moon"]["last"]["days_ago"],
            moon_moon_phase_full_moon_last_name = response["moon_phases"]["full_moon"]["last"]["name"],
            moon_moon_phase_full_moon_last_description = response["moon_phases"]["full_moon"]["last"]["description"],
            moon_moon_phase_full_moon_next_timestamp = response["moon_phases"]["full_moon"]["next"]["timestamp"],
            moon_moon_phase_full_moon_next_datestamp = response["moon_phases"]["full_moon"]["next"]["datestamp"],
            moon_moon_phase_full_moon_next_days_ahead = response["moon_phases"]["full_moon"]["next"]["days_ahead"],
            moon_moon_phase_full_moon_next_name = response["moon_phases"]["full_moon"]["next"]["name"],
            moon_moon_phase_full_moon_next_description = response["moon_phases"]["full_moon"]["next"]["description"],
            location_latitude = response["location"]["latitude"],
            location_longitude = response["location"]["longitude"])
        
        new_record.save()

    create_record()
    context = dict()
    context["count"] = Advanced.objects.count()
    return render(request, 'dashboard/dashboard.html', context)