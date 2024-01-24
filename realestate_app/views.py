from django.shortcuts import render
from .models import Property
from random import shuffle
import requests

# Create your views here.
def index(request):
    all_properties = Property.objects.all()
    # Convert queryset to a list for shuffling
    properties_list = list(all_properties)
    # Shuffle the list of properties
    shuffle(properties_list)
    #select 3 properties
    selected_properties = properties_list[:3]
    return render(request, 'index.html', {'properties': selected_properties})

def about_us(request):
    return render(request, 'about_us.html')

def contact_us(request):
    return render(request, 'contact.html')


    