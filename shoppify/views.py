from .models import Shop
from rest_framework import viewsets, permissions
from .serializers import ShopSerializer

class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes=[permissions.AllowAny]