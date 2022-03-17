from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.

def view_bag(request):
    """ A view that renders bag contents """
    return render(request, 'bag/bag.html')


def add_to_bag(request, event_id):
    """ Add a quantity of the specified event to the orders """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if event_id in list(bag.keys()):
        bag[event_id] += quantity
    else:
        bag[event_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, event_id):
    """ Adjust quantity of tickets in shopping bag """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[event_id] = quantity
    else:
        bag.pop(event_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, event_id):
    """ Remove tickets from shopping bag """

    try:
        bag = request.session.get('bag', {})
        bag.pop(event_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)
    
    except Exception as e:
        return HttpResponse(status=500)