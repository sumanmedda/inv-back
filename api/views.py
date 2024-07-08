from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserModel, ProductModel
from .serializers import UserSerializers, ProductSerializers

# Create your views here.

class ProductView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = ProductSerializers(data)
            print(1, serializer.data)
            if serializer.is_valid():
                print(2, serializer.data)
                serializer.save()
                return Response({"status":200,"message": "Product Added", "product":serializer.data})
            else:
                return Response({"status":404,"message": "Something Went Wrong"})
        except:
            return Response({"status":404,"message": "Something Went Wrong"})
        
    # def get(self, request, pk):
    #     try:
    #         product = ProductModel.objects.get(id=pk)
    #         serializer = ProductSerializers(product)
    #         return Response({"status":200,"message": "Fetched Product", "product":serializer.data})
    #     except:
    #         return Response({"status":404,"message": "Item Not Found"})

    
    def put(self, request, pk):
        try:
            product = ProductModel.objects.get(id=pk)
            product.id = request.data["id"]
            product.product_id = request.data["product_id"]
            product.product_name = request.data["product_name"]
            product.product_desc = request.data["product_desc"]
            product.product_qty = request.data["product_qty"]
            product.product_price = request.data["product_price"]
            product.product_img = request.data["product_img"]
            product.save()
            return Response({"status":200,"message": "Products Updated", "products": 'product'})
        except:
            return Response({"status":404,"message": "Something Went Wrong"})
    
    
    def delete(self, request, pk):
        try:
            product = ProductModel.objects.get(id=pk)
            product.delete()
            return Response({"status":200,"message": "Product Deleted"})
        except:
            return Response({"status":404,"message": "Something Went Wrong"})
    



class AllProducts(APIView):
    def get(self, request):
        try:
            products = ProductModel.objects.all()
            serializer = ProductSerializers(products, many=True)
            return Response({"status":200,"message": "All Products Fetched", "products":serializer.data})
        except:
            return Response({"status":404,"message": "Item Not Found"})
            