from django.db import models
from django.contrib.auth.models import User

class Categroy(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categroies'
        
    def __str__(self):
        return self.name

class Item(models.Model):
    Categroy = models.ForeignKey(Categroy, related_name="items", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank = True, null= True)
    price = models.FloatField()
    images = models.ImageField(upload_to = "Image_items", blank = True, null = True )
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)    
    
    
    def __str__(self):
        return self.name
