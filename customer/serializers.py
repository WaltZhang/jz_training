from rest_framework import serializers

from .models import IdentityRegistry

class IdentityRegistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentityRegistry
        fields = '__all__'
