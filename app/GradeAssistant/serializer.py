from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import (
    Class,
    Grade,
    Student,
)

class ClassSerializer(ModelSerializer):
    """Convert Model instances of type `Class` into python datatypes

    """
    class Meta:
        model = Class
        fields = "__all__"

class GradeSerializer(ModelSerializer):
    """Convert Model instances of type `Grade` into python datatypes

    """
    class Meta:
        model = Grade
        fields = "__all__"

class StudentSerializer(ModelSerializer):
    """Convert Model instances of type `Student` into python datatypes

    """

    class Meta:
        model = Student
        fields = "__all__"

class UserLoginSerializer(ModelSerializer):
    """Convert Model instances of type `User` into python datatypes

    """
    username = serializers.CharField()
    password = serializers.CharField()
    token = serializers.CharField(read_only=True)

    def check_data(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if username is None:
            raise serializers.ValidationError('A username is required to log in.')
        
        if password is None:
            raise serializers.ValidationError('A password is required to log in.')

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError('A user with this username and password was not found.')

        if not user.is_active:
            raise serializers.ValidationError('This user has been deactivated.')

        user = authenticate(username=username, password=password)

        return user
    class Meta:
        model = User
        fields = ("id", "username", "password", "token")

class UserSerializer(ModelSerializer):
    """Convert Model instances of type `User` into python datatypes

    """
    class Meta:
        model = User
        fields = ("id", "username", "password", "token")