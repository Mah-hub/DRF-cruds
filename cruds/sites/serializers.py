from rest_framework.serializers import ModelSerializer
from .models import Site

class siteSeralizer(ModelSerializer):
    class Meta:
        model = Site
        fields ='__all__'
        depth = 1