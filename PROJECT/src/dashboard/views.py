from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import ProductTable
from .serializers import ProductSerializer

import json

# Create your views here.

def dashboard_view(request):
    return render(request, "dashboard/dashboard.html", {})

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def product_manager(request):

    if request.method == 'GET':
        try:
            if request.GET['product']:

                product_name = request.GET['product']

                try:
                    product = ProductTable.objects.get(pk=product_name)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                
                serializer = ProductSerializer(product)
                return Response(serializer.data)
        
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'POST':

        new_product = request.data

        serializer = request.data

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':

        name = request.data['product_name']

        try:
            updated_product = ProductTable.objects.get(pk=name)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductSerializer(updated_product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':

        try:
            product_to_delete = ProductTable.objects.get(pk=request.data['product_name'])
            product_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)