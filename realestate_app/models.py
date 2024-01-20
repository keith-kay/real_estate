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
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=200)
    payment_plan = models.CharField(max_length=200)
    amenities = models.TextField()
    property_type = models.ForeignKey(Property_type, on_delete=models.CASCADE )
    photo = models.ImageField(upload_to='property_photos/', null=True)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title 
    
