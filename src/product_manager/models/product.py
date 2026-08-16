from django.db import models

from product_manager.models.category import Category


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=610)
    sku = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)

    image = models.ImageField(
        upload_to="products/",
        null=True,
        blank=True,
    )

    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,
        related_name="products"
    )
    
    def __str__(self):
        return f"{self.title}, {self.description}, {self.price}"
