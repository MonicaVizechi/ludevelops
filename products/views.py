from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer, SellerSerializer
from .models import Seller, Product

class ProductViewSet(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailViewSet(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SellerViewSet(generics.ListCreateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class SellerDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer