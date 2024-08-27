from django.http import HttpResponse
from . import views
from .models import Advanced
from django.shortcuts import render
from .controllers import create_basic_dict, create_sun_dict, create_moon_dict

def index(request):
    return HttpResponse("This is the dashboard")

def basic(request, advanced_id):
    context = create_basic_dict(advanced_id)
    return render(request, "dashboard/basic.html", context)

def sun(request, advanced_id):
    context = create_sun_dict(advanced_id)
    return render(request, "dashboard/sun.html", context)

def moon(request, advanced_id):
    context = create_moon_dict(advanced_id)
    return render(request, "dashboard/moon.html", context)

def eclipses(request, advanced_id):
    advanced = Advanced.objects.get(id=advanced_id)
    context = {"advanced" : advanced.moon_phase_name,
               "moon_age": advanced.moon_phase_age_days}
    return render(request, "dashboard/eclipses.html", context)


