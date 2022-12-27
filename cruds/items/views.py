from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Item
from .serializers import itemSerializer
# Create your views here.

class itemListApiView(ListAPIView):
    serializer_class = itemSerializer
    queryset = Item.objects.all()