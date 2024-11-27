from rest_framework import serializers

from .models import ProductTable


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTable
        fields = '__all__'