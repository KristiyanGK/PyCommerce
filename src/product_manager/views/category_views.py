from rest_framework.decorators import api_view
from rest_framework.response import Response

from product_manager.models.category import Category
from product_manager.serializers.category_serializer import CategorySerializer


@api_view(['POST'])
def add_category(request):
    category = CategorySerializer(data=request.data)
    
    if not category.is_valid():
        return Response(category.errors, status=400)
    
    if Category.objects.filter(name=category.validated_data['name']).exists():
        return Response({'error': 'Category with this name already exists.'}, status=400)
    
    category.save()
    return Response(category.validated_data, status=201)
