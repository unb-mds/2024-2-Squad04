from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import ProductTable
from .serializers import ProductSerializer

import logging

logger = logging.getLogger(__name__)

# Create your views here.

def dashboard_view(request):
    return render(request, "dashboard/dashboard.html", {})

class ProductManager(APIView):

    def get(self, request):

        product_name = request.GET.get('product')

        if not product_name:
            logger.error("GET request failed: product name not provided")
            return Response({'error': 'Product name not provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = ProductTable.objects.get(product_name=product_name)
            serializer = ProductSerializer(product)
            logger.info(f"GET request successful: Product {product_name} retrieved")
            return Response(serializer.data)
        except ProductTable.DoesNotExist:
            logger.warning(f"GET request failed: Product {product_name} not found")
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

            
    def post(self, request):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            logger.info(f"POST request successful: Product '{serializer.data['product_name']}' created.")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        logger.error(f"POST request failed: Invalid data fot Product '{serializer.data['product_name']}'")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        product_name = request.data.get('product_name')

        if not product_name:
            logger.warning("PUT request failed: product name not provided")
            return Response({'error': 'Product name not provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = ProductTable.objects.get(product_name=product_name)
        except ProductTable.DoesNotExist:
            logger.warning(f"PUT request failed: Product {product_name} not found")
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            logger.info(f"PUT request successful: Product {product_name} updated successfully")
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        logger.error(f"PUT request failed: Invalid data fot Product {product_name}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        product_name = request.data.get('product_name')

        if not product_name:
            logger.warning("DELETE request failed: product name not provided")
            return Response({'error': 'Product name not provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = ProductTable.objects.get(product_name=product_name)
            product.delete()
            logger.info(f"DELETE request successful: Product {product_name} deleted successfully")
            return Response({'message': 'Product deleted successfully'}, status=status.HTTP_202_ACCEPTED)
        except ProductTable.DoesNotExist:
            logger.warning(f"DELETE request failed: Product {product_name} not found")
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
