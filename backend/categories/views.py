from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import viewsets

from .models import Category
from .serializers import CategorySerializer

# Create your views here.
class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    
    def list(self, response):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    def create(self, response):
        serializer = CategorySerializer(data=response.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    
    def retrieve(self, response):
        category = Category.objects.get(id=response.data['id'])
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    def update(self, response):
        category = Category.objects.get(id=response.data['id'])
        serializer = CategorySerializer(category, data=response.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def partial_update(self, request):
        category = Category.objects.get(id=request.data['id'])
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, response):
        category = Category.objects.get(id=response.data['id'])
        category.delete()
        return Response(status=204)