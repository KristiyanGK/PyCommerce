from django.urls import include, path
from rest_framework import routers

from product_manager.views import category_views, product_views

router = routers.DefaultRouter()
router.register("products", product_views.ProductViewSet)
router.register("categories", category_views.CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
