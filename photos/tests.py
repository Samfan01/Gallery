from django.test import TestCase
from .models import Photo,Category,Location

# Create your tests here.

class PhotoTestClass(TestCase):
    
    def setUp(self):
        #creating a new Photo and saving it
        self.photo = Photo(photo = 'photo',photo_category = 'foods',photo_location = 'Nairobi')
        self.photo.save_photo()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.photo,Photo))
        
    def test_save_method(self):
        self.photo.save_photo()
        photos = Photo.objects.all()
        self.assertTrue(len(photos) > 0)
        
class CategoryTestClass(TestCase):
    
    def setUp(self):
        self.category = Category(category = 'social')
        self.category.save_category()
        
class LocationTestClass(TestCase):
    
    def setUp(self):
        self.location = Location(location_name = 'Nairobi')
        self.location.save_location()