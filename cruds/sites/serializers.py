from rest_framework import serializers
from .models import Site
from items.serializers import itemSerializer


class siteSeralizer(serializers.ModelSerializer):
    #items = itemSerializer(many=True)

    class Meta:
        model = Site
        fields ='__all__'
        depth = 1