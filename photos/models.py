from django.db import models

# Create your models here. 


class Photo(models.Model):
    photo = models.ImageField(upload_to = 'photos/')
    name = models.CharField(max_length = 60)
    description = models.CharField(max_length = 60)
    category = models.ForeignKey('Category' ,on_delete=models.CASCADE,)
    location = models.ForeignKey('Location' ,on_delete=models.CASCADE,)
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
         
    @classmethod
    def search_by_category(cls,search_term):
        photos = cls.objects.filter(category__category__icontains =search_term)
        return photos
   
    # @classmethod
    # def show_by_location(cls,photo_location):
    #     photos = cls.objects.filter(photo_location)
    #     return photos
    
class Category(models.Model):
    category = models.CharField(max_length = 30)
    
    
    def __str__(self):
        return self.category
    
    class Meta:
        ordering = ['category']
             
    @classmethod
    def search_by_category(cls,search_term):
        photos = cls.objects.filter(category=search_term)
        return photos
    
class Location(models.Model):
    location_name = models.CharField(max_length = 30)
    
    def __str__(self):
        return self.location_name
    
    class Meta:
        ordering = ['location_name']
        
    @classmethod
    def by_location(self,location):
        photos = cls.objects.filter(location)
        return photos