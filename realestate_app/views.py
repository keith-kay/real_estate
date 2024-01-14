from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about_us.html')