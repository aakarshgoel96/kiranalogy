from django.contrib.auth.models import User
from rest_framework import serializers

from utils.message import *


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=30)
    password1 = serializers.CharField(write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})
    email = serializers.EmailField()

    class Meta:
        model = User
        exclude = (
            'password',
            'groups',
            'user_permissions',
            'last_login',
            'is_superuser',
            'date_joined',
            'is_staff',
            'is_active'
        )

    def validate_email(self, email):
        if User.objects.filter(email=email):
            raise serializers.ValidationError(USER_ALREADY_EXIST_ERROR_MSG)
        return email

    def validate(self, attrs):
        if attrs.get('password1') != attrs.get('password2'):
            return serializers.ValidationError('password must be same')
        return attrs

    def save(self, request):
        validated_data = dict(username=request.data['username'], email=request.data['email'])
        validated_data['password'] = request.data['password1']
        validated_data['first_name'] = request.data.get('first_name')
        user = User.objects.create_user(**validated_data)
        return user
