from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from product_manager.models.category import Category
from product_manager.serializers.category_serializer import CategorySerializer


@extend_schema_view(
    list=extend_schema(summary="List categories"),
    retrieve=extend_schema(summary="Retrieve a category"),
    create=extend_schema(summary="Create a category"),
    update=extend_schema(summary="Replace a category"),
    partial_update=extend_schema(summary="Update a category"),
    destroy=extend_schema(summary="Delete a category"),
)
@extend_schema(tags=["categories"])
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
