from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator



class Rating(models.Model):
    title = models.CharField(max_length=50, default='None')
    content = models.CharField(max_length=300)
    author = models.ForeignKey('user.User', on_delete=models.CASCADE,)
    grade = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    shoes_avaliated = models.ForeignKey('shoes.Shoes', on_delete=models.CASCADE, null=True,)
      
    def __str__(self):
        return self.title