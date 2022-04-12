from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Event

from .models import Event
from .forms import EventForm

def all_events(request):
    """ A view to return all the events on TicketSpark for buyers """
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

    return render(request, 'events/all_events.html', context)

def my_events(request):
    """ A view to return all the events that belong to creators """
    events = Event.objects.filter(user=request.user).values()
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

    return render(request, 'events/my_events.html', context)


def event_detail(request, event_id):
    """ A view to return buyer event details """
    event = get_object_or_404(Event, pk=event_id)

    context = {
        'event': event,
    }

    return render(request, 'events/event_detail.html', context)


def my_event_detail(request, event_id):
    """ A view to return creator event details """
    event = get_object_or_404(Event, pk=event_id)

    context = {
        'event': event,
    }

    return render(request, 'events/my_event_detail.html', context)


@login_required
def add_event(request):
    """ Create an event """
    user = request.user
    if not request.user.is_superuser:
            messages.error(request, 'Sorry, only event creators can do that.')
            return redirect(reverse('home'))

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            messages.success(request, 'Successfully created event!')
            return redirect(reverse('event_detail', args=[event.id]))
        else:
            messages.error(request, 'Failed to create event. Please ensure the form is valid.')
    else:
        form = EventForm()

    template = 'events/add_event.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_event(request, event_id):
    """ Edit an event """
    if not request.user.is_superuser:
            messages.error(request, 'Sorry, only event creators can do that.')
            return redirect(reverse('home'))

    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated event!')
            return redirect(reverse('event_detail', args=[event.id]))
        else:
            messages.error(request, 'Failed to update event. Please ensure the form is valid.')
    else:
        form = EventForm(instance=event)
        messages.info(request, f'You are editing {event.name}')

    template = 'events/edit_event.html'
    context = {
        'form': form,
        'event': event,
    }

    return render(request, template, context)


@login_required
def delete_event(request, event_id):
    """ Delete an event """
    if not request.user.is_superuser:
            messages.error(request, 'Sorry, only event creators can do that.')
            return redirect(reverse('home'))
   
    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    messages.success(request, 'Event removed!')
    return redirect(reverse('events'))