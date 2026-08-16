from django.urls import path, include
from rest_framework import routers

from product_manager.views import product_views, category_views

router = routers.DefaultRouter()
router.register('products', product_views.ProductViewSet)
router.register('categories', category_views.CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
