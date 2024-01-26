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

def property_detail(request, property_title):
    property_instance = get_object_or_404(Property, title=property_title)

    property_images = property_instance.image_set.all()
    site_map_images = property_instance.image_set.filter(title='Site Map')
    aerial_view_images = property_instance.image_set.filter(title='overview')
    # Add more filters for additional titles as needed

    context = {
        'property': property_instance,
        'property_images': property_images,
        'site_map_images': site_map_images,
        'aerial_view_images': aerial_view_images,
        # Add more variables for additional titles as needed
    }

    return render(request, 'property_detail.html', context)


    