from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories')
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True, blank=True)
    product_name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField( upload_to='products' )
    
    def __str__ (self):
        return self.product_name


# Create your models here.
