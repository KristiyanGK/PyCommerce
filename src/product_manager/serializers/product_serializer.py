from rest_framework import serializers

from product_manager.models.product import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "description", "sku", "price", "category", "image"]
