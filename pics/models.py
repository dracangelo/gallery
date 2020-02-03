from django.db import models

# Create your models here.

CATEGORIES = (
            ('beauty', 'beauty'),
            ('daily', 'daily'),
            ('art', 'art'),
            ('food', 'food'),
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
