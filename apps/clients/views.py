from .models import Client, ClientSocialNetwork
from rest_framework import viewsets
from .serializer import ClientSerializer, ClientSocialnetworkSerializer

# Create your views here.

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer  

class ClientSocialnetworkViewSet(viewsets.ModelViewSet):
    queryset = ClientSocialNetwork.objects.all()
    serializer_class = ClientSocialnetworkSerializer

