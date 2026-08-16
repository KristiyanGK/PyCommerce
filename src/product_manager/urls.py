from django.urls import path

from product_manager.views import product_views, category_views

urlpatterns = [
    # product endpoints
    path(route='products/create', view=product_views.add_product, name='add_product'),
    path(route='products/list/', view=product_views.get_products, name='get_products'),
    
    # category endpoints
    path(route='categories/create', view=category_views.add_category, name='add_category'),
]
