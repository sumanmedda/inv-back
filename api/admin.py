from django.contrib import admin
from .models import UserModel, ProductModel
# Register your models here.

admin.site.register(UserModel)
admin.site.register(ProductModel)
