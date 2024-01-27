from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Land(models.Model):
    title = models.CharField(max_length = 200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dimensions = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='videos/')
    
    def __str__(self):
        return self.title
  
class Property_type(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name 
    
class Property(models.Model):
    title = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=200)
    payment_plan = models.CharField(max_length=200)
    amenities = models.TextField()
    coordinates=models.CharField(max_length=600, unique=True, null=True)
    property_type = models.ForeignKey(Property_type, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Image(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_photos/')
    title = models.CharField(max_length=200, default='Default Title')

    def __str__(self):
        return f"Image for {self.property.title}"
