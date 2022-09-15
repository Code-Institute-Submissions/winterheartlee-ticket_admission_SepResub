from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from events.models import Event


def view_bag(request):
    """ A view that renders bag contents """
    return render(request, 'bag/bag.html')


def add_to_bag(request, event_id):
    """ Add a quantity of the specified event to the orders """
    event = get_object_or_404(Event, pk=event_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if event_id in list(bag.keys()):
        bag[event_id] += quantity
        messages.success(request, f'Adjusted {event.name} ticket quantity to x{bag[event_id]}')
    else:
        bag[event_id] = quantity
        messages.success(request, f'Added {event.name} ticket to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, event_id):
    """ Adjust quantity of tickets in shopping bag """

    event = get_object_or_404(Event, pk=event_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[event_id] = quantity
        messages.success(request, f'Adjusted {event.name} ticket quantity to x{bag[event_id]}')
    else:
        bag.pop(event_id)
        messages.success(request, f'Removed {event.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, event_id):
    """ Remove tickets from shopping bag """

    event = get_object_or_404(Event, pk=event_id)

    try:
        bag = request.session.get('bag', {})
        bag.pop(event_id)
        messages.success(request, f'Removed all tickets for {event.name}')

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing event: {e}')
        return HttpResponse(status=500)
