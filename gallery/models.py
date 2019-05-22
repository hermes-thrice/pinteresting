from django.db import models


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()


class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

class Image(models.Model):
    image= models.ImageField(default = 'default.jpg', upload_to = 'images')
    title = models.CharField(max_length =60)
    description = models.CharField(max_length=100,blank = True)
    location= models.ForeignKey(Location, on_delete=models.CASCADE)
    category= models.ForeignKey(Category,on_delete=models.CASCADE)
    # pub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

    @classmethod
    def all_images(cls):
        photo_gallery=cls.objects.all()
        return photo_gallery

    class Meta:
        ordering = ['title']

    @classmethod
    def search_by_title(cls,search_term):
        photo_gallery=cls.objects.filter(title__icontains=search_term)
        return photo_gallery

    @classmethod
    def filter_by_location(cls,location):
        locate_image=cls.objects.filter(location__icontains=location)
        return locate_image
    
    @classmethod
    def delete_image(cls,title):
        deleted_image=cls.objects.filter(title = title).delete()
        return deleted_image

#  We filter the model data using the __icontains query filter. 
# This filter will check if any word in the titlefield of our articles matches the search_term.