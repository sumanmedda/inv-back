from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserModel
from .serializers import UserSerializers

class AllUsers(APIView):
    def get(self, request):
        try:
            users = UserModel.objects.all()
            serializer = UserSerializers(users, many=True)
            return Response({"status":200,"message": "All Users Fetched", "users":serializer.data})
        except Exception as e:
            return Response({"status":200,"message": "No User Found", "error":str(e)})

class AddUser(APIView):
    def post(self, request):
        data = request.data
        try:
            serializer = UserSerializers(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status":201,"message": "Users Created", "users":serializer.data})
            else:
                return Response({"status":404,"message": "Something went wrong", "error":serializer.errors})
        except Exception as e:
                return Response({"status":404,"message": "Something went wrong", "error":str(e)})



class UserView(APIView):
    def get(self, request, pk):
        try:
            user = UserModel.objects.get(id=pk)
            serializer = UserSerializers(user)
            return Response({"status":200,"message": "Fetched User", "product":serializer.data})
        except Exception as e:
            return Response({"status":404,"message": "No User Found", "error":str(e)})

    
    def put(self, request, pk):
        try:
            user = UserModel.objects.get(id=pk)
            user.user_id = request.data["user_id"]
            user.first_name = request.data["first_name"]
            user.last_name = request.data["last_name"]
            user.email = request.data["email"]
            user.password = request.data["password"]
            user.is_Admin = request.data["is_Admin"]
            user.created_at = request.data["created_at"]
            user.save()
            return Response({"status":200,"message": "User Updated", "user": request.data})
        except Exception as e:
            return Response({"status":404,"message": "No User Found", "error":str(e)})


    def delete(self, request, pk):
        try:
            user = UserModel.objects.get(id=pk)
            user.delete()
            return Response({"status":200,"message": "User Deleted"})
        except Exception as e:
            return Response({"status":404,"message": "No User Found", "error":str(e)})



