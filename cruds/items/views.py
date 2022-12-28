from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView
from .models import Item
from .serializers import itemSerializer
from sites.serializers import siteSeralizer
from sites.models import Site
# Create your views here.

class itemListApiView(ListAPIView):
    serializer_class = itemSerializer
    queryset = Item.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add a list of users to the context, using the UserSerializer to serialize the data
        context['items'] = siteSeralizer(self.object.items.all(), many=True).data
        return context


class itemRetrieveAPIView(RetrieveAPIView):
    serializer_class = itemSerializer
    lookup_field='code'
    queryset = Item.objects.all()
    
