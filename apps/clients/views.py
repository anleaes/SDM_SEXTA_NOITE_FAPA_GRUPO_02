from .models import Client, ClientSocialnetwork
from rest_framework import viewsets
from .serializer import ClientSerializer, ClientSocialnetworkSerializer

# Create your views here.

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer  
