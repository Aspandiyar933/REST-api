from rest_framework import serializers
from .models import Location, Item

class ItemSerializer(serializers.Serializer):
    class Meta:
        model = Item
        fields = ('__all__')    

    
class LocationSerializer(serializers.Serializer):
    class Meta:
        model = Location
        fields = ('__all__') 