from rest_framework import serializers

from product_manager.models.category import Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'parent']  # noqa: RUF012
