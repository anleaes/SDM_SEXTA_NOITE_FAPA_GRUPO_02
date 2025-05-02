from django.shortcuts import render
from .models import Product
from rest_framework import viewsets
from .serializer import ProductSerializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer  
