from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import City, Event
from .forms import EventForm
import json


def index(request):
    city = None
    events = None
    if 'city' in request.GET:
        city = request.GET['city']
        events = Event.objects.filter(city__city=city)

    else:
        events = Event.objects.filter(city__city='Noida')
        city = events.get(pk=1).city

    return render(request, 'events/index.html', {'events': events,
                                                 'city': city})


def get_city(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        places = City.objects.filter(city__istartswith=q)
        results = []
        for pl in places:
            place_json = {}
            place_json = pl.city
            results.append(place_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def event_details(request, id):
    event = Event.objects.get(pk=id)
    return render(request, 'events/event_details.html', {'event': event})


@login_required(login_url="login")
def create(request):
    if request.method == 'GET':
        form = EventForm()
        return render(request, 'events/create_event.html', {'form': form})
    else:
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.save()
            return redirect('index')
        else:
            return render(request, 'events/create_event.html', {'form': form})
