from .models import ClientSocialnetwork
from rest_framework import viewsets
from .serializer import ClientSocialnetworkSerializer

# Create your views here.

class ClientSocialnetworkViewSet(viewsets.ModelViewSet):
    queryset = ClientSocialnetwork.objects.all()
    serializer_class = ClientSocialnetworkSerializer
