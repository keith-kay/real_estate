from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Land(models.Model):
    title = models.CharField(max_length = 200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    price = models.CharField(max_length=500)
    payment_plan = models.TextField(null=True)
    titledeed=models.CharField(max_length=500, null=True)
    coordinates=models.CharField(max_length=600, null=True)
    size = models.CharField(max_length=200)
    
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
    price = models.CharField(max_length=400, )
    price_details = models.TextField(null=True, default='empty')
    size = models.TextField()
    payment_plan = models.TextField(null=True)
    amenities = models.TextField()
    coordinates=models.CharField(max_length=600, null=True)
    nearby=models.TextField(null=True)
    property_type = models.ForeignKey(Property_type, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Image(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=True)
    land = models.ForeignKey(Land, on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='property_photos/')
    title = models.CharField(max_length=200, default='Default Title')

    def __str__(self):
        if self.property:  # Check if property is not None
            return f"Image for {self.property.title}"
        else:
            return f"Image for Land: {self.land.title}"
    
class Video(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=True)
    land = models.ForeignKey(Land, on_delete=models.CASCADE, null=True)
    video = models.FileField(upload_to='property_videos/')
    title = models.CharField(max_length=200, default='Default Title')

    def __str__(self):
        if self.property:  # Check if property is not None
            return f"Image for {self.property.title}"
        else:
            return f"Image for Land: {self.land.title}"
