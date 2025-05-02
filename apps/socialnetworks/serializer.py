from .models import SocialNetwork
from rest_framework import serializers

class SocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = '__all__'