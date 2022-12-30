from rest_framework.serializers import ModelSerializer,PrimaryKeyRelatedField
from .models import Item,Site

class itemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__' 

class siteSerializer(ModelSerializer):
    items = itemSerializer(many=True)
    class Meta:
        model = Site
        fields ='__all__'

""" class ItemSiteSerializer(ModelSerializer):
    class Meta:
        model = ItemSite
        fields = ['item', 'site', 'quantity'] """

#Here before using the .set i tried to use itembysite serializer 
""" class ItemSiteSerializer(ModelSerializer):

    items = PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )

    sites = PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Item
        fields = ['id', 'items', 'code', 'sites'] """
        