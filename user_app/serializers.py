from rest_framework import serializers
from .models import UserInformation
from django.contrib.auth.models import User


class UserInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInformation
        fields = ['id', 'username', 'email', 'mobile', 'role']


from rest_framework import serializers


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # Ensure password field is write-only

    def create(self, validated_data):
        # This method is necessary when using ModelSerializer
        return User.objects.create_user(**validated_data)

    #username = serializers.CharField(max_length=150)
    #password = serializers.CharField(write_only=True, style={'input_type': 'password'})