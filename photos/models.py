from django.db import models

# Create your models here. 


class Photo(models.Model):
    photo = models.ImageField(upload_to = 'photos/')
    photo_location = models.CharField(max_length = 60)
    photo_category = models.CharField(max_length = 60)
    upload_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.photo_location 
 
    class Meta:
        ordering = ['photo_location']
    
    def save_photo(self):
        self.save()
        
    @classmethod
    def photo_info(cls):
        photos = cls.objects.all()
        return photos
           