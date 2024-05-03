from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth.models import auth
from django.shortcuts import render, redirect
from django.shortcuts import redirect
from rest_framework.permissions import IsAuthenticated


def register_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'register.html')
 

def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'login.html')


@api_view(['GET'])
def home_page(request):
    if not request.user.is_authenticated:
        return redirect('login/')
    return render(request, 'home.html')


@api_view(['POST'])
def register(request):
    user_serializer = UserSerializer(data=request.data)
    
    if user_serializer.is_valid():
        user_serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    
    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(
            {'error': 'Username or password is invalid.'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
def logout(request):
    auth.logout(request)
