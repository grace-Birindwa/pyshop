from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.ImageField(upload_to='image_fruit', blank=True)


class Offer(models.Model):
    code = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    discount = models.FloatField()




