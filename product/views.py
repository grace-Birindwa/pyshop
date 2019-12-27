from django.shortcuts import render
from django.http import HttpResponse
from .models import Products

def index(request):
    product = Products.objects.all()
    # context = {'products': product}
    return render(request, 'index.html', {'products': product})

def new(request):
    return HttpResponse('New product')
