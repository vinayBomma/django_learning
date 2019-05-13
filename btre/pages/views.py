from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from realtors.models import Realtor

def index(request):
    listing = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listing
    }
    return render(request, 'pages/index.html', context)

def about(request):
    realtor = Realtor.objects.order_by('hired_date')
    mvp = Realtor.objects.filter(is_mvp=True)

    context = {
        'realtors': realtor,
        'mvps': mvp
    }
    return render(request, 'pages/about.html', context) 