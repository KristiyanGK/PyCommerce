from django.db.models import Q, QuerySet
from django_filters import CharFilter, NumberFilter
from django_filters.rest_framework import FilterSet

from product_manager.models.category import Category
from product_manager.models.product import Product


class ProductFilter(FilterSet):
    search = CharFilter(
        method="filter_search",
        label="Search",
    )

    category = CharFilter(
        method="filter_category",
        label="Category",
    )

    min_price = NumberFilter(
        field_name="price",
        lookup_expr="gte",
        label="Minimum price",
    )

    max_price = NumberFilter(
        field_name="price",
        lookup_expr="lte",
        label="Maximum price",
    )

    @staticmethod
    def filter_search(
        queryset: QuerySet[Product],
        name: str,
        value: str,
    ) -> QuerySet[Product]:
        return queryset.filter(
            Q(title__icontains=value) |
            Q(sku__icontains=value)
        )

    @staticmethod
    def filter_category(
        queryset: QuerySet[Product],
        name: str,
        value: str,
    ) -> QuerySet[Product]:
        try:
            category = Category.objects.get(name=value)
        except Category.DoesNotExist:
            return queryset.none()

        categories = [category, *category.get_descendants()]

        return queryset.filter(category__in=categories)

    class Meta:
        model = Product
        fields = ["search", "min_price", "max_price"]
