from django.shortcuts import render
from .models import Property
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about_us.html')

def contact_us(request):
    return render(request, 'contact.html')

def property_list(request):
    properties = Property.objects.all()
    return render(request, 'index.html', {'properties': properties})