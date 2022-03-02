from django.shortcuts import render, get_object_or_404
from .models import Event

# Create your views here.

def all_events(request):
    """ A view to return all the events that belong to user """
    events = Event.objects.all()

    context = {
        'events': events,
    }

    return render(request, 'events/events.html', context)


def event_detail(request, event_id):
    """ A view to return single event details """
    event = get_object_or_404(Event, pk=event_id)

    context = {
        'event': event,
    }

    return render(request, 'events/event_detail.html', context)