""" from django.shortcuts import render
from .serializers import siteSeralizer
from rest_framework.generics import ListAPIView,RetrieveAPIView
from .models import Site
# Create your views here.

class siteListAPIView(ListAPIView):
    serializer_class = siteSeralizer
    queryset = Site.objects.all()

class siteRetriveAPIView(RetrieveAPIView):
    serializer_class = siteSeralizer
    lookup_field= 'code'
    queryset = Site.objects.all()
        
     """