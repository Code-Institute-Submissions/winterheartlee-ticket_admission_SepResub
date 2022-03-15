from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from events.models import Event

def bag_contents(request):

    bag_items = []
    total = 0
    ticket_count = 0
    bag = request.session.get('bag', {})

    for event_id, quantity in bag.items():
        event = get_object_or_404(Event, pk=event_id)
        total += quantity * event.price
        ticket_count += quantity
        bag_items.append({
            'event_id': event_id,
            'quantity': quantity,
            'event': event,
        })

    if total:
        delivery = Decimal(settings.STANDARD_DELIVERY)
        free_delivery = settings.FREE_DELIVERY - total
    else:
        delivery = 0
    
    grand_total = delivery + total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'ticket_count': ticket_count,
        'delivery': delivery,
        'free_delivery': settings.FREE_DELIVERY,
        'grand_total': grand_total,
    }

    return context