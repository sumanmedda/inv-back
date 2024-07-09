from django.urls import path
from .product_views import AllProducts, ProductView, AddProduct

urlpatterns = [
    path('all-products/', AllProducts.as_view(), name="all-products"),
    path('add-products/', AddProduct.as_view(), name="add-products"),
    path('product/<str:pk>/', ProductView.as_view(), name="product"),
    path('update-product/<str:pk>/', ProductView.as_view(), name="update-product"),
    path('delete-product/<str:pk>/', ProductView.as_view(), name="delete-product"),
]
