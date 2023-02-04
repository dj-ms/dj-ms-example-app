from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.api.views.category_views import CategoryViewSet
from app.api.views.product_views import ProductViewSet

router = DefaultRouter(trailing_slash=False)

router.register('categories', CategoryViewSet, basename='category')

router.register('products', ProductViewSet, basename='product')


urlpatterns = [
    path('', include(router.urls)),
]
