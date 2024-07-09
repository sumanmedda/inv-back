from django.urls import path
from .product_views import AllProducts, ProductView, AddProduct
from .user_views import AllUsers, AddUser, UserView
urlpatterns = [
    # Product Apis
    path('all-products/', AllProducts.as_view(), name="all-products"),
    path('add-products/', AddProduct.as_view(), name="add-products"),
    path('product/<str:pk>/', ProductView.as_view(), name="product"),
    path('update-product/<str:pk>/', ProductView.as_view(), name="update-product"),
    path('delete-product/<str:pk>/', ProductView.as_view(), name="delete-product"),
    # User Apis
    path('all-users/', AllUsers.as_view(), name="all-users"),
    path('add-users/', AddUser.as_view(), name="add-users"),
    path('user/<str:pk>/', UserView.as_view(), name="user"),
    path('update-user/<str:pk>/', UserView.as_view(), name="update-user"),
    path('delete-user/<str:pk>/', UserView.as_view(), name="delete-user"),
]
