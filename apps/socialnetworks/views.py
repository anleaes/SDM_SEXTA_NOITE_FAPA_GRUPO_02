from django.shortcuts import render
from .models import SocialNetwork
from rest_framework import viewsets
from .serializer import SocialNetworkSerializer

# Create your views here.
class SocialNetworkViewSet(viewsets.ModelViewSet):
    queryset = SocialNetwork.objects.all()
    serializer_class = SocialNetworkSerializer  
