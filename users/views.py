from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth.models import auth
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@api_view(['POST'])
def register(request):
    user_serializer = UserSerializer(data=request.data)
    
    if user_serializer.is_valid():
        user_serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    
    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def register_page(request):
    return render(request, 'register.html')


def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/') 
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            return redirect('/login')
    else:
        return render(request, 'login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('/login') 


@login_required(login_url='/login')
def home_page(request):
    return render(request, 'home.html')