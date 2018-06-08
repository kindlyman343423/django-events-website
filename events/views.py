from django.shortcuts import render
from django.http import HttpResponse
from .models import Location
import json


def index(request):
    return render(request, 'events/index.html')


def search(request):
    if request.method == 'POST':
        location = request.POST['location']
        print(location)
    return HttpResponse('')


def get_location(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        places = Location.objects.filter(location__contains=q)
        results = []
        for pl in places:
            place_json = {}
            place_json = pl.location
            results.append(place_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
