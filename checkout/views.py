from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "No events in your bag")
        return redirect(reverse('events'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Kii3DF0oYB4ravREGiFIFp6XlGBDkniLQWlK2PRrn9Kn8fEoA7Y0Kg9PbLXY0awaH40nRFcWTz2VUMX8LWXuxbu00x0lU5CT1',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)