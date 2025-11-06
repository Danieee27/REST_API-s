from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 30)
    price = models.IntegerField(default = 0)
    description = models.CharField(max_length = 30)
    size_range = models.CharField(max_length = 6, default = 0)
    
    def __str__(self):
        return self.name

class Profile(models.Model):
    Username = models.CharField(max_length = 30)
    Phone = models.IntegerField(default = 0)
    Email_Address = models.EmailField(max_length = 50)
    Address = models.CharField(max_length = 200)

    def __str__(self):
        return self.Username

class Order(models.Model):
    Product = models.CharField(max_length = 30)
    Preferred_size = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.Product
  