from django.db import models

# Create your models here. 


class Photo(models.Model):
    photo = models.ImageField(upload_to = 'photos/')
    photo_location = models.CharField(max_length = 60)
    photo_category = models.CharField(max_length = 60)
    
