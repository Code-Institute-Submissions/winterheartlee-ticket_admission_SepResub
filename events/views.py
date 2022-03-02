from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Event

# Create your views here.

def all_events(request):
    """ A view to return all the events that belong to user """
    events = Event.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('events'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            events = events.filter(queries)

    context = {
        'events': events,
        'search_term': query,
    }

    return render(request, 'events/events.html', context)


def event_detail(request, event_id):
    """ A view to return single event details """
    event = get_object_or_404(Event, pk=event_id)

    context = {
        'event': event,
    }

    return render(request, 'events/event_detail.html', context)