from rest_framework import generics
from .models import Location, Item
from .serializers import LocationSerializer, ItemSerializer

class ItemList(generics.ListCreateAPIView):
    serialaizer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        location = self.request.query_params.get('location', None)