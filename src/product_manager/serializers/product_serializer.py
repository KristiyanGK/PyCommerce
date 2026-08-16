from rest_framework import serializers

from product_manager.models.product import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'description', 'sku', 'price', 'category']  # noqa: RUF012
