
from django.http import HttpResponse
from django.shortcuts import render
from .models import Location, Character

def index(request):
    """ This views return the home page """
    return render(request, "app/index.html")

def content(request):
    """ this views return the application content """
    context = {}
    all_planets = Location.objects.all()
    list_type = set()
    for i in all_planets:
        try:
            list_type.add(i.location_type)
        except:
            pass
    context['planets'] = all_planets
    dict_type_planet = {}
    for i in list_type:
        dict_type_planet[i] = Location.objects.filter(location_type=i)
    context['list_type_planet'] = dict_type_planet
    return render(request, 'app/content.html', context)

