from django.db import models

def get_image_filename(self, filename):
        ext = filename.split('.')[-1]
        new_filename = f"{self.shoes_name}.{ext}"
        return f'images/{new_filename}'

class Shoes(models.Model):
    shoes_name = models.CharField(max_length= 50, default='Generico')
    brand = models.CharField(max_length=50)
    gender = models.CharField(max_length = 20)
    size = models.IntegerField
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    photo = models.ImageField(upload_to=get_image_filename,default=None, null=True, blank=True)
    
    def __str__(self):
        return self.shoes_name
