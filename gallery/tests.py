from django.test import TestCase
from .models import  Location,Category,Image
# Create your tests here.

#test our location model
class LocationTestCase(TestCase):

    #setup method
    def setUp(self):
        self.cairo=Location(name='cairo')
    
    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.cairo,Location))

    #testing save method
    def test_save_method(self):
        self.cairo.save_location()
        locations=Location.objects.all()
        self.assertTrue(len(locations) > 0)
    
    #testing for update method

    def tearDown(self):
        Location.objects.all().delete()

#test our category model
class CategoryTestCase(TestCase):

    #setup method
    def setUp(self):
        self.nature=Category(name='nature')
    
    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nature,Category))

    #testing save method
    def test_save_method(self):
        self.nature.save_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories) > 0)
    
    #testing for update method

    #testing for delete function
    def tearDown(self):
        Category.objects.all().delete()