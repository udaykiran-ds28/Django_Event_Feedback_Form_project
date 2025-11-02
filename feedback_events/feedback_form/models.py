from django.db import models

# Create your models here.
class Event(models.Model): 
    title = models.CharField(max_length=100) 
    description = models.TextField() 
    date = models.DateField() 
    location = models.CharField(max_length=100) 
    created_at = models.DateTimeField(auto_now_add=True) 
 
    def __str__(self): 
        return self.title