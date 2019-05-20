from django.db import models


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name


class Image(models.Model):
    image= models.ImageField(default = 'default.jpg', upload_to = 'images')
    title = models.CharField(max_length =60)
    description = models.CharField(max_length=100)
    location= models.ForeignKey(Location, on_delete=models.CASCADE)
    category= models.ForeignKey(Category,on_delete=models.CASCADE)
    # pub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

    # @classmethod
    # def all_images(cls):



