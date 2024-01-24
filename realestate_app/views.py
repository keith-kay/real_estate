from django.shortcuts import render, get_object_or_404
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

def property_list(request):
    properties= Property.objects.all()
    return render(request, 'properties.html', {'properties': properties} )

def property_detail(request, property_id):
    property_instance = get_object_or_404(Property, id=property_id)

    # You can add more context data if needed
    context = {
        'property': property_instance,
    }
    return render(request, 'property_detail.html', context)


    