from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView
from .models import Item,Site
from .serializers import itemSerializer,siteSerializer

# Create your views here.

class itemListApiView(ListAPIView):
    serializer_class = itemSerializer
    queryset = Item.objects.all()

class itemRetrieveAPIView(RetrieveAPIView):
    serializer_class = itemSerializer
    lookup_field='code'
    queryset = Item.objects.all()

class siteListAPIView(ListAPIView):
    serializer_class = siteSerializer
    queryset = Site.objects.all()

class siteRetriveAPIView(RetrieveAPIView):
    serializer_class = siteSerializer
    lookup_field= 'code'
    queryset = Site.objects.all()

   
        
    
""" class ItemSiteView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSiteSerializer
    lookup_field = 'code'

class SiteItemView(RetrieveAPIView):
    queryset = Site.objects.all()
    serializer_class = ItemSiteSerializer
    lookup_field = 'code' """