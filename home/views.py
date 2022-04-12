from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')

def creator_homepage(request):
    """ A view to return the index page """
    return render(request, 'home/creator_homepage.html')

def buyer_homepage(request):
    """ A view to return the index page """
    return render(request, 'home/buyer_homepage.html')