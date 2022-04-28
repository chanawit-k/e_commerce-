from django.db import models
from django.forms import CharField

# Create your models here.
class Products (models.Model):

    
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    images = models.CharField(max_length=300)

