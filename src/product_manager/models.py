from django.db import models


# Create your models here.    
class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children"
    )
    
    def __str__(self):
        return f"{self.name}, {self.parent}"
    
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=610)
    image = models.ImageField
    sku = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,
        related_name="products"
    )
    
    def __str__(self):
        return f"{self.title}, {self.description}, {self.price}"
