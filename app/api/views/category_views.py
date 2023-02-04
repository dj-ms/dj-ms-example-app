from rest_framework import viewsets, permissions

from app.api.serializers.category_serializers import CategorySerializer
from app.models import Category


class CategoryViewSet(viewsets.ModelViewSet):
    model = Category
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

