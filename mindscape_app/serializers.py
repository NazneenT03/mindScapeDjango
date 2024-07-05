from rest_framework import serializers
from .models import UserModel




class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields ='__all__'
















# class UserRegistrationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'password']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         # Create and return a new user instance using the validated data
#         user = CustomUser.objects.create_user(**validated_data)
#         return user