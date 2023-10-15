from django.db import models

# Create your models here.

class Shop(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    year = models.IntegerField()
    image = models.CharField()
    origin = models.CharField(max_length=200)
    available_items = models.IntegerField()
