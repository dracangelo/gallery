from django.db import models


# Create your models here.

CATEGORIES = (
            ('party', 'party'),
            ('daily', 'daily'),
            ('art', 'art'),
            ('comics', 'comics'),
            ('culture', 'culture'),
            ('scenery', 'scenery'),
        )
        
class Category(models.Model):
    catname = models.CharField(max_length=40, choices=CATEGORIES) 
        
    def __str__(self):
        return self.catname
        
    def save_category(self):
        self.save()    
        
    def delete_category(self):
        Category.objects.filter(id = self.pk).delete()
            
    def update_category(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)


LOCATIONS = (
            ('nairobi', 'nairobi'),
            ('somewhere', 'somewhere'),
            ('belgium', 'belgium'),
            ('wild', 'wild'),
            ('france', 'france'),
            ('mombasa', 'mombasa'),
        )
        
class Location(models.Model):
    locname = models.CharField(max_length=40, choices=LOCATIONS) 
        
    def __str__(self):
        return self.locname
        
    def save_location(self):
        self.save()    
        
    def delete_location(self):
        Location.objects.filter(id = self.pk).delete()
           
    def update_location(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)

class Image(models.Model):
    image = models.ImageField(upload_to = 'picha/', null = True, blank = True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    category = models.ForeignKey('Category', on_delete = models.CASCADE, null='True', blank=True)
    location = models.ForeignKey('Location', on_delete = models.CASCADE, null='True', blank=True)
        
    def __str__(self):
        return self.name
        
    def save_image(self):
        self.save()   
        
    def delete_image(self):
        Image.objects.filter(id = self.pk).delete() 
            
    def update_image(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)       
        
    @classmethod
    def all_pics(cls):
        pics = cls.objects.all()
        return pics 
        
    @classmethod
    def search_by_category(cls, search_input):
        images = cls.objects.filter(category__catname__icontains=search_input)
        return images        
        
        class Meta:
            ordering = ['catname']