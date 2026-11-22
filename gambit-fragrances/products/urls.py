from django.urls import path
from .views import ProductListCreateView
from .views import ProductDetailView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]