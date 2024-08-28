"""
practice
"""
import json
from datetime import datetime

def update():
    """
    loads json
    """
    json_object = open("advanced_real2.json")
    request = json.load(json_object)

    #print(request.keys())
    print(datetime.fromtimestamp(request["timestamp"]))
    print(request["datestamp"])
    #print(request["sun"])
    print(request["sun"]["sunrise"])
    print(request["sun"]["sunrise_timestamp"])
    print(request["sun"]["sunset"])
    print(request["sun"]["sunset_timestamp"])
    print(request["sun"]["solar_noon"])
    print(request["sun"]["day_length"])
    print(request["sun"]["sun_altitude"])
    print(request["sun"]["sun_distance"])
    print(request["sun"]["sun_azimuth"])
    print(request["sun"]["next_solar_eclipse"]["timestamp"])
    print(request["sun"]["next_solar_eclipse"]["datestamp"])
    print(request["sun"]["next_solar_eclipse"]["type"])
    print(request["sun"]["next_solar_eclipse"]["visibility_regions"])
#   {'sunrise': 1724817900, 'sunrise_timestamp': '06:05', 'sunset': 1724867760, 'sunset_timestamp': '19:56', 'solar_noon': '13:01', 'day_length': '13:51', 'sun_altitude': -23.561721145730246, 'sun_distance': 151150857.10669097, 'sun_azimuth': 327.2998115628817, 
#   'next_solar_eclipse': {'timestamp': 1727887573, 'datestamp': 'Wed, 02 Oct 2024 18:46:13 +0200', 'type': 'Annular Solar Eclipse', 'visibility_regions': 'Pacific, s South America ; [Annular: s Chile, s Argentina]'}}
    #print(request["moon"])
    print(request["moon"]["phase"])
    print(request["moon"]["phase_name"])
    print(request["moon"]["stage"])
    print(request["moon"]["illumination"])
    print(request["moon"]["age_days"])
    print(request["moon"]["lunar_cycle"])
    print(request["moon"]["emoji"])
    print(request["moon"]["zodiac"]["sun_sign"])
    print(request["moon"]["zodiac"]["moon_sign"])
    print(request["moon"]["moonrise"])
    print(request["moon"]["moonrise_timestamp"])
    print(request["moon"]["moonset"])
    print(request["moon"]["moonset_timestamp"])
    print(request["moon"]["moon_altitude"])
    print(request["moon"]["moon_distance"])
    print(request["moon"]["moon_azimuth"])
    print(request["moon"]["moon_parallactic_angle"])
    print(request["moon"]["next_lunar_eclipse"]["timestamp"])
    print(request["moon"]["next_lunar_eclipse"]["datestamp"])
    print(request["moon"]["next_lunar_eclipse"]["type"])
    print(request["moon"]["next_lunar_eclipse"]["visibility_regions"])
#   {'phase': 0.8037274132496317, 'phase_name': 'Waning Crescent', 'stage': 'waning', 'illumination': '33%', 'age_days': 24, 'lunar_cycle': '80.37%', 'emoji': '🌘', 
#   'zodiac': {'sun_sign': 'Virgo', 'moon_sign': 'Gemini'}, 
#   'moonrise': '23:17', 'moonrise_timestamp': 1724879820, 'moonset': '16:39', 'moonset_timestamp': 1724855940, 'moon_altitude': -1.4584079647693682, 'moon_distance': 383688.7488001796, 'moon_azimuth': 37.26194734909308, 'moon_parallactic_angle': -25.366518424807126, 
#   'next_lunar_eclipse': {'timestamp': 1726620326, 'datestamp': 'Wed, 18 Sep 2024 02:45:26 +0200', 'type': 'Partial Lunar Eclipse', 'visibility_regions': 'Americas, Europe, Africa'}}
    #print(request["moon_phases"])
    print(request["moon_phases"]["new_moon"]["last"]["timestamp"])
    print(request["moon_phases"]["new_moon"]["last"]["datestamp"])
    print(request["moon_phases"]["new_moon"]["last"]["days_ago"])
    print(request["moon_phases"]["new_moon"]["next"]["timestamp"])
    print(request["moon_phases"]["new_moon"]["next"]["datestamp"])
    print(request["moon_phases"]["new_moon"]["next"]["days_ahead"])
    print(request["moon_phases"]["full_moon"]["last"]["timestamp"])
    print(request["moon_phases"]["full_moon"]["last"]["datestamp"])
    print(request["moon_phases"]["full_moon"]["last"]["days_ago"])
    print(request["moon_phases"]["full_moon"]["last"]["name"])
    print(request["moon_phases"]["full_moon"]["last"]["description"])
    print(request["moon_phases"]["full_moon"]["next"]["timestamp"])
    print(request["moon_phases"]["full_moon"]["next"]["datestamp"])
    print(request["moon_phases"]["full_moon"]["next"]["days_ahead"])
    print(request["moon_phases"]["full_moon"]["next"]["name"])
    print(request["moon_phases"]["full_moon"]["next"]["description"])
#   {'new_moon': {'last': {'timestamp': 1722722400, 'datestamp': 'Sun, 04 Aug 2024 00:00:00 +0200', 'days_ago': 24}, 
#   'next': {'timestamp': 1725314400, 'datestamp': 'Tue, 03 Sep 2024 00:00:00 +0200', 'days_ahead': 5}}, 
#   'first_quarter': {'last': {'timestamp': 1723413600, 'datestamp': 'Mon, 12 Aug 2024 00:00:00 +0200', 'days_ago': 16}, 
#   'next': {'timestamp': 1726005600, 'datestamp': 'Wed, 11 Sep 2024 00:00:00 +0200', 'days_ahead': 13}}, 
#   'full_moon': {'last': {'timestamp': 1724018400, 'datestamp': 'Mon, 19 Aug 2024 00:00:00 +0200', 'days_ago': 9, 'name': 'Sturgeon Moon', 'description': 'Marks the time when sturgeon fish are most easily caught.'}, 
#   'next': {'timestamp': 1726610400, 'datestamp': 'Wed, 18 Sep 2024 00:00:00 +0200', 'days_ahead': 20, 'name': 'Harvest Moon', 'description': 'Refers to the full moon closest to the autumnal equinox, signalling the time to harvest crops.'}}, 
#   'last_quarter': {'last': {'timestamp': 1724623200, 'datestamp': 'Mon, 26 Aug 2024 00:00:00 +0200', 'days_ago': 2}, 
#   'next': {'timestamp': 1727128800, 'datestamp': 'Tue, 24 Sep 2024 00:00:00 +0200', 'days_ahead': 26}}}
    #print(request["location"])
    print(request["location"]["latitude"])
    print(request["location"]["longitude"])
#   {'latitude': 51.5, 'longitude': 0}
