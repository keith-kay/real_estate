from django.shortcuts import render, get_object_or_404
from .models import Property, Land
from random import shuffle
from .forms import ContactForm 
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
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
    #get all lands
    all_lands = Land.objects.all()
    # convert queryset to list for shuffling
    lands_list = list(all_lands)
    # shuffle the list of lands
    shuffle(lands_list)
    # select 3 lands
    selected_lands = lands_list[:3]
    context= {
        'properties': selected_properties,
        'lands': selected_lands 
    }
    return render(request, 'index.html', context)

def about_us(request):
    return render(request, 'about_us.html')

def property_list(request):
    properties= Property.objects.all()
    return render(request, 'properties.html', {'properties': properties} )

def land_list(request):
    lands= Land.objects.all()
    return render(request, 'lands.html', {'lands': lands})

def land_detail(request, land_id):
    land_instance = get_object_or_404(Land, pk=land_id)
    land_images = land_instance.image_set.all()
    context = {'land': land_instance,
               'land_images': land_images
               }
    
    return render(request, "land_detail.html", context)

def property_detail(request, property_title):
    property_instance = get_object_or_404(Property, title=property_title)

    property_images = property_instance.image_set.all()
    site_map_images = property_instance.image_set.filter(title='Site Map')
    aerial_view_images = property_instance.image_set.filter(title='overview')
    first_floors= property_instance.image_set.filter(title='1stflr')
    second_floors= property_instance.image_set.filter(title='2ndflr')
    third_floors= property_instance.image_set.filter(title='3rdflr')
    fourth_floors= property_instance.image_set.filter(title='4thflr')
    fifth_floors= property_instance.image_set.filter(title='5thflr')
    # Add more filters for additional titles as needed

    context = {
        'property': property_instance,
        'property_images': property_images,
        'site_map_images': site_map_images,
        'aerial_view_images': aerial_view_images,
        'first_floors': first_floors,
        'second_floors': second_floors,
        'third_floors': third_floors,
        'fourth_floors': fourth_floors,
        'fifth_floors' : fifth_floors,
        # Add more variables for additional titles as needed
    }

    return render(request, 'property_detail.html', context)

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Compose the email message
            email_body = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"
            
            # Send the email
            send_mail(
                subject='Contact Form Submission',  # Email subject
                message=email_body,  # Email message body
                from_email=email,  # Sender's email address
                recipient_list=['keithrhova@gmail.com'],  # Recipient email addresses
                fail_silently=False,  # Raise an error if email sending fails
            )
            
            # Redirect to a thank you page
            return HttpResponseRedirect('/thank-you/')  # Adjust the URL as needed
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})


    