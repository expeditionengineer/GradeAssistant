from django.shortcuts import render
from django.contrib.auth import authenticate, get_user_model, login, logout
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.authtoken.models import Token


from .serializer import (
    ClassSerializer,
    GradeSerializer,
    StudentSerializer,
    UserLoginSerializer,
    UserSerializer,
)
from .models import *

def validate_username(data):
    username = data['username'].strip()
    if not username:
        raise ValidationError('choose another username')
    return True

def validate_password(data):
    password = data['password'].strip()
    if not password:
        raise ValidationError('a password is needed')
    return True

@api_view(["GET"])
def get_routes(request):
    """First Implementation of an API-Endpoint.

    """

    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)

@api_view(["GET"])
def get_dashboard_info(request):
    """

    """
    if request.user.is_authenticated:
        studentObjects = Student.objects.filter(user=request.user)
        gradeObjects = Grade.objects.filter(user=request.user)
        classesObjects = Class.objects.filter(user=request.user)

        classSerializer = ClassSerializer(classesObjects, many=True)
        gradeSerializer = GradeSerializer(gradeObjects, many=True)
        studentSerializer = StudentSerializer(studentObjects, many=True)

        return Response(
            {
                "class": classSerializer.data, 
                "grade": gradeSerializer.data, 
                "student": studentSerializer.data,
            }
        )
    else:
        return Response([{"Login": False}])

# @api_view(["POST"])
# def login(request):
#     """

#     """
#     if request.user.is_authenticated:
#         return Response([{"Login": True}])
#     else:
#         username = request.data["email"]
#         password = request.data["password"]
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             return Response([{"Login": True}])
#         else:
#             return Response([{"Login": False}])

class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)
    ##
    def post(self, request):
        data = request.data
        assert validate_username(data)
        assert validate_password(data)
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            print(data)
            user = serializer.check_data(data)
            token, created = Token.objects.get_or_create(user=user)
            # user = authenticate(username=data["username"], password=data["password"])
            # login(request, user)
            return Response({"username": data["username"], "token": token.key}, status=status.HTTP_200_OK)

@api_view(["POST"])
def add_grade(request):
    """

    """
    # print(request)
    if request.user.is_authenticated:
        # data = request.data
        print(request)
        serializer = GradeSerializer(data=request)
        
        if serializer.is_valid(raise_exception=True):
            serializer.create()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response([{"Login": False}])