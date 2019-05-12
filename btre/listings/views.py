from django.shortcuts import render

def index(request):
    return render(request, 'listings/listings.html')

def list(request):
    return render(request, 'listings/list.html')

def search(request):
    return render(request, 'listings/search.html')