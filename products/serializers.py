from rest_framework import serializers
from .models import Product, Seller

class SellerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seller
        fields = ['seller_id', 'name']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id', 'name', 'price', 'stock_quantity', 'status', 'seller']