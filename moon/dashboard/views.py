from django.http import HttpResponse
from . import views
from .models import Advanced
from django.shortcuts import render
from .controllers import create_basic_dict, create_sun_dict, create_moon_dict
import requests
from django.http import JsonResponse
from dotenv import load_dotenv
import os
import json
def index(request):
    context = dict()
    context["count"] = Advanced.objects.count()
    return render(request, 'dashboard/dashboard.html', context)

def basic(request, advanced_id):
    context = create_basic_dict(advanced_id)
    context["count"] = Advanced.objects.count()
    return render(request, "dashboard/basic.html", context)

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
    url = "https://moon-phase.p.rapidapi.com/advanced"

    querystring = {"lat":"51.4583","lon":"-2.5591"}

    headers = {
	    "x-rapidapi-key": os.environ.get('API_KEY'),
	    "x-rapidapi-host": "moon-phase.p.rapidapi.com"
}

#    response = requests.get(url, headers=headers, params=querystring)
#    response = 
#    print(response.json())
