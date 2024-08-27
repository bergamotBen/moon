from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:advanced_id>/", views.basic, name="basic"),
    path("sun/<int:advanced_id>/", views.sun, name="sun"),
    path("moon/<int:advanced_id>/", views.moon, name="moon"),
    path("eclipses/<int:advanced_id>/", views.eclipses, name="eclipses"),
]