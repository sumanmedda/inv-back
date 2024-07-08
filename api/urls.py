from django.urls import path
from .views import AllProducts, ProductView

urlpatterns = [
    path('all-products/', AllProducts.as_view(), name="all-products"),
    path('add-products/', ProductView.as_view(), name="add-products"),
    path('product/<str:pk>/', ProductView.as_view(), name="product"),
    path('update-product/<str:pk>/', ProductView.as_view(), name="update-product"),
    path('delete-product/<str:pk>/', ProductView.as_view(), name="delete-product"),
]
