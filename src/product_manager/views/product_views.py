from rest_framework.decorators import api_view
from rest_framework.response import Response

from product_manager.models.product import Product
from product_manager.serializers.product_serializer import ProductSerializer


@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_product(request):
    product = ProductSerializer(data=request.data)
    
    if not product.is_valid():
        return Response(product.errors, status=400)
    
    if Product.objects.filter(sku=product.validated_data['sku']).exists():
        return Response({'error': 'Product with this SKU already exists.'}, status=400)
    
    product.save()
    return Response(product.validated_data, status=201)
