from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import UserModel
from .serializers import UserModelSerializer
from django.contrib.auth import login as django_login

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        try:
            user = UserModel.objects.get(user_name = username)
            user_serializer = UserModelSerializer(user)
            if user.password== password:
                # django_login(request,user)
                return Response({"data":user_serializer.data})
        except UserModel.DoesNotExist:
            return Response("no user")
        
@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        email = request.data['email']
        user = UserModel.objects.create(user_name=username,password=password,email=email)
        user.save()
        # django_login(request,user)
        user_serializer = UserModelSerializer(user)
        return Response({"data":user_serializer.data})
        

@api_view(['GET'])
def retrieve_update_acc(request, id):
    if request.method == 'GET':
        try:
            user = UserModel.objects.get(user_name=id)
            user_serializer = UserModelSerializer(user)
            
           
            return Response({"data":user_serializer. data})
        except UserModel.DoesNotExist:
            # user = UserModel.objects.create(email=id, name='new user', contactNo=000000)
            # user.save()
            # user_serializer = UserModelSerializer(user)
            return Response({"data": "user not exists"})

    # elif request.method == 'PUT':
    #     try:
    #         user = UserModel.objects.get(email=id)
    #     except UserModel.DoesNotExist:
    #         return Response({"error": "User not found."})

    #     data = {
    #         'name': request.data.get('name'),
    #         'email': request.data.get('email'),
    #         'pic': request.data.get('pic'),
    #         'contactNo': request.data.get('contact'),
    #     }
    #     user_serializer = UserModelSerializer(user, data=data, partial=True)
    #     if user_serializer.is_valid():
    #         user_serializer.save()
    #         return Response(user_serializer.data)
    #     return Response(user_serializer.errors)
    



























# class UserRegistrationViewSet(viewsets.ViewSet):
#     serializer_class = UserRegistrationSerializer

#     def create(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             # Save the user to the database
#             serializer.save()
#             return Response({'success': 'User registered successfully'})
#         else:
#             return Response(serializer.errors, status=400)