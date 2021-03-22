from django.db import models

# Create your models here. 


class Photo(models.Model):
    photo = models.ImageField(upload_to = 'photos/')
    name = models.CharField(max_length = 60)
    description = models.CharField(max_length = 60)
    upload_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name 
 
    class Meta:
        ordering = ['name']
    
    def save_photo(self):
        self.save()
        
    @classmethod
    def photo_info(cls):
        photos = cls.objects.all()
        return photos
    # @classmethod
    # def search_by_category(cls,search_term):
    #     photos = cls.objects.filter(photo_category__icontains=search_term)
    #     return photos
    # @classmethod
    # def show_by_location(cls,photo_location):
    #     photos = cls.objects.filter(photo_location)
    #     return photos
class Category(models.Model):
    category = models.CharField(max_field = 30)
    
    def __str__(self):
        return self.category