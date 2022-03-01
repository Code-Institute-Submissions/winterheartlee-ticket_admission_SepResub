from django.shortcuts import render
from .models import Event

# Create your views here.

def all_events(request):
    """ A view to return all the events that belong to user """
    events = Event.objects.all()

    context = {
        'events': events,
    }

    return render(request, 'events/events.html', context)