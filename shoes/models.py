from django.db import models

class Shoes(models.Model):
    shoes_name = models.CharField(max_length= 50, default='Generico')
    brand = models.CharField(max_length=50)
    gender = models.CharField(max_length = 20)
    size = models.IntegerField
    
    def __str__(self):
        return self.shoes_name
