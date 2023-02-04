from rest_framework import serializers

from app.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'slug', 'description', 'image', 'price', 'category')


