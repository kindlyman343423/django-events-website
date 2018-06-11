from django.shortcuts import render
from django.http import HttpResponse
from .models import Location, Event
import json


def index(request):
    if request.method == 'GET':
        events = Event.objects.filter(location__location='Noida')
        location = events.get(pk=1).location
        return render(request, 'events/index.html', {'events': events,
                                                     'location': location})
    else:
        location = request.POST['location']
        events = Event.objects.filter(location__location=location)
        return render(request, 'events/index.html', {'events': events,
                                                     'location': location})


def get_location(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        places = Location.objects.filter(location__istartswith=q)
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


def event_details(request, id):
    event = Event.objects.get(pk=id)
    return render(request, 'events/event_details.html', {'event': event})
