from rest_framework import serializers
from .models import UserModel, ProductModel

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = "__all__"