from django.contrib import admin

from product_manager.models.category import Category
from product_manager.models.product import Product

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
