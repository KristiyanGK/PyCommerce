from decimal import Decimal

from django.db.models import QuerySet
from django.test import TestCase

from product_manager.filters.product_filters import ProductFilter
from product_manager.models.category import Category
from product_manager.models.product import Product


class ProductSearchFilterTests(TestCase):
    electronics: Category
    office: Category
    laptop: Product
    mouse: Product
    keyboard: Product

    def setUp(self):
        self.electronics = Category.objects.create(name="Electronics")
        self.office = Category.objects.create(name="Office")

        self.laptop = Product.objects.create(
            title="Gaming Laptop",
            description="A powerful laptop",
            sku="LAP-001",
            price=Decimal("1299.99"),
            category=self.electronics,
        )
        self.mouse = Product.objects.create(
            title="Wireless Mouse",
            description="Ergonomic mouse with laptop stand",
            sku="MOU-100",
            price=Decimal("29.99"),
            category=self.electronics,
        )
        self.keyboard = Product.objects.create(
            title="Mechanical Keyboard",
            description="RGB keyboard",
            sku="KEY-LAP",
            price=Decimal("89.99"),
            category=self.office,
        )

    def _filter_search(
        self,
        value: str,
        queryset: QuerySet[Product] | None = None,
    ) -> QuerySet[Product]:
        queryset = queryset if queryset is not None else Product.objects.all()
        return ProductFilter.filter_search(queryset, "search", value)

    def _filter_category(
        self,
        value: str,
        queryset: QuerySet[Product] | None = None,
    ) -> QuerySet[Product]:
        queryset = queryset if queryset is not None else Product.objects.all()
        return ProductFilter.filter_category(queryset, "category", value)

    def _filterset_qs(self, **data: str) -> QuerySet[Product]:
        return ProductFilter(
            data=data,
            queryset=Product.objects.all(),
        ).qs

    def test_search_matches_title_case_insensitive(self):
        queryset = self._filter_search("laptop")

        self.assertEqual(list(queryset), [self.laptop])

    def test_search_matches_partial_title(self):
        queryset = self._filter_search("Wireless")

        self.assertEqual(list(queryset), [self.mouse])

    def test_search_matches_sku(self):
        queryset = self._filter_search("MOU-100")

        self.assertEqual(list(queryset), [self.mouse])

    def test_search_matches_partial_sku_case_insensitive(self):
        queryset = self._filter_search("key-lap")

        self.assertEqual(list(queryset), [self.keyboard])

    def test_search_matches_title_or_sku(self):
        queryset = self._filter_search("lap")

        self.assertEqual(list(queryset.order_by("id")), [self.laptop, self.keyboard])

    def test_search_does_not_match_description(self):
        queryset = self._filter_search("ergonomic")

        self.assertEqual(list(queryset), [])

    def test_search_returns_empty_queryset_when_nothing_matches(self):
        queryset = self._filter_search("no-such-product")

        self.assertFalse(queryset.exists())

    def test_search_applies_to_existing_queryset(self):
        queryset = self._filter_search(
            "lap",
            queryset=Product.objects.filter(category=self.electronics),
        )

        self.assertEqual(list(queryset), [self.laptop])

    def test_filterset_search_by_title(self):
        queryset = self._filterset_qs(search="mouse")

        self.assertEqual(list(queryset), [self.mouse])

    def test_filterset_search_by_sku(self):
        queryset = self._filterset_qs(search="LAP-001")

        self.assertEqual(list(queryset), [self.laptop])

    def test_filterset_omits_search_when_value_is_empty(self):
        queryset = self._filterset_qs(search="")

        self.assertEqual(queryset.count(), 3)

    def test_category_matches_exact_name(self):
        queryset = self._filter_category("Electronics")

        self.assertEqual(list(queryset.order_by("id")), [self.laptop, self.mouse])

    def test_category_matches_name_case_insensitive(self):
        queryset = self._filter_category("electronics")

        self.assertEqual(list(queryset.order_by("id")), [self.laptop, self.mouse])

    def test_category_matches_uppercase_name(self):
        queryset = self._filter_category("ELECTRONICS")

        self.assertEqual(list(queryset.order_by("id")), [self.laptop, self.mouse])

    def test_category_returns_empty_queryset_when_nothing_matches(self):
        queryset = self._filter_category("no-such-category")

        self.assertFalse(queryset.exists())

    def test_filterset_category_case_insensitive(self):
        queryset = self._filterset_qs(category="office")

        self.assertEqual(list(queryset), [self.keyboard])
