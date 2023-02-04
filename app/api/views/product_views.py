from rest_framework import viewsets, permissions

from app.api.serializers.product_serializers import ProductSerializer
from app.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    model = Product
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


