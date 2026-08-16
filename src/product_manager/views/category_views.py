from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from product_manager.models.category import Category
from product_manager.serializers.category_serializer import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
