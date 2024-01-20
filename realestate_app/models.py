from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class land(models.Model):
    title = models.CharField(max_length = 200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dimensions = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='videos/')
    
    def __str__(self):
        return self.title