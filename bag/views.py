from django.shortcuts import render, redirect

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
    print(request.session['bag'])
    return redirect(redirect_url)