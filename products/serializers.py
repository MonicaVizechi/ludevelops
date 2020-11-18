from rest_framework import serializers
from .models import Product, Seller

class SellerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seller
<<<<<<< HEAD
        fields = ['seller_id', 'name','url']
=======
        fields = ['id','name','url']
>>>>>>> e97fccbafb35558f4abd01195d366bcb84fb089f


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
<<<<<<< HEAD
        fields = ['product_id', 'name', 'price', 'stock_quantity', 'status', 'seller','url']
=======
        fields = ['id','code', 'name', 'price', 'stock_quantity', 'status', 'seller']
>>>>>>> e97fccbafb35558f4abd01195d366bcb84fb089f
