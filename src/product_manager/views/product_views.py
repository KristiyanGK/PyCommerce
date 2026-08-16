from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated

from product_manager.filters.product_filters import ProductFilter
from product_manager.models.product import Product
from product_manager.serializers.product_serializer import ProductSerializer


@extend_schema_view(
    list=extend_schema(
        summary="List products",
        description=(
            "Return products. Filter with `search` (title or SKU), "
            "`min_price`, `max_price`, and `category` (name, including descendants)."
        ),
    ),
    retrieve=extend_schema(summary="Retrieve a product"),
    create=extend_schema(summary="Create a product"),
    update=extend_schema(summary="Replace a product"),
    partial_update=extend_schema(summary="Update a product"),
    destroy=extend_schema(summary="Delete a product"),
)
@extend_schema(tags=["products"])
class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    parser_classes = [
        MultiPartParser,
        FormParser
    ]
