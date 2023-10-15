from .models import Shop
from rest_framework import serializers

class ShopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shop
        fields = ('id','name','price','year','image','origin','available_items')

